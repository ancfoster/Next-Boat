from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from PIL import Image
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Listings, ListingMedia
from django.db.models import Q
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime

from .models import Listings
from .forms import ListingCreateForm, ListingMediaForm


# Create your views here.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.filter(Q(listing_status='A') | Q(listing_status='P'))
    template_name = "listings/listings.html"


class MyListings(LoginRequiredMixin, generic.ListView):
    model = Listings
    template_name = 'listings/my_listings.html'
    def get_queryset(self):
        return Listings.objects.filter(created_by=self.request.user)


class ListingDetails(View):
    def get(self, request, id, *args, **kwargs):
        queryset = Listings.objects.all()
        listing = get_object_or_404(queryset, id=id)
        gallery_images = listing.listing_media.all()
        preview_images = listing.listing_media.all()[:4]        
        return render(
            request,
            "listings/listing_details.html",
            {
                "listing": listing,
                "gallery_images": gallery_images,
                "preview_images": preview_images
            },
        )


#This view deletes listings
class ListingDelete(LoginRequiredMixin, DeleteView):
    template_name = 'listings/listing_delete.html'
    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Listings, id=id_)

    def get_success_url(self):
        return reverse('my_listings')


#This view creates a new listing
@login_required
def createListing(request):
    if request.method == 'POST':
        listing_create_form = ListingCreateForm(request.POST, request.FILES)
        listing_media_form = ListingMediaForm(request.POST, request.FILES)
        if listing_create_form.is_valid() and listing_media_form.is_valid():
            listing_create_form.instance.listing_status = 'A'
            listing_create_form.instance.created_by = request.user
            featured_image = listing_create_form.cleaned_data['featured_image']
            getMake = listing_create_form.cleaned_data['make']
            getModel = listing_create_form.cleaned_data['model']
            now = datetime.now()
            info_string = f"{getMake}-{getModel}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}"
            compressed_featured_image = compress_featured_image(featured_image)
            listing_create_form.instance.featured_image = compressed_featured_image
            listing_create_form.instance.featured_image.field.upload_to = info_string+'/'
            form = listing_create_form.save()
            form.save()
            new_listing_id = form.pk
            # loop over images to upload multiple
            for image_uploaded in request.FILES.getlist('image'):
                listing_name = f"{listing_create_form.instance.make}_{listing_create_form.instance.model}_{listing_create_form.instance.pk}"
                compressed_image = compress_uploaded_images(image_uploaded, listing_name)
                image_instance = ListingMedia.objects.create(listing=form, image=compressed_image)
                image_instance.image.field.upload_to = info_string+'/'
                image_instance.save()
            return redirect('boat_listings')
    else:
        listing_create_form = ListingCreateForm()
        listing_media_form = ListingMediaForm()
    context = {'listing_create_form': listing_create_form, 'listing_media_form': listing_media_form}
    return render(request, 'listings/listing_create_form.html', context)


def home(request):
    return render(request, 'listings/index.html')

#This function take an image and string as an argument and then compressed using PILLOW library
def compress_uploaded_images(image, listing_name):
    image = Image.open(image)
    #.thumbnail method resizes the uploaded images, values are max height & width
    image.thumbnail((1024, 1024))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=70)
    #listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, f"{listing_name}.jpeg", 'image/jpeg', image_io.tell(), None)
    return image_file

def compress_featured_image(image):
    image = Image.open(image)
    #.thumbnail method resizes the uploaded images, values are max height & width
    image.thumbnail((1024, 1024))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=65)
    #listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, 'featured_image.jpeg', 'image/jpeg', image_io.tell(), None)
    return image_file