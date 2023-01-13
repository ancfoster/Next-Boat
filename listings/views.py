from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ListingCreateForm, ListingMediaForm
from PIL import Image
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Listings, ListingMedia
from django.db.models import Q
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your views here.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.filter(Q(listing_status='A') | Q(listing_status='P'))
    template_name = "listings/listings.html"


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


@login_required
def createListing(request):
    if request.method == 'POST':
        listing_create_form = ListingCreateForm(request.POST, request.FILES)
        listing_media_form = ListingMediaForm(request.POST, request.FILES)
        if listing_create_form.is_valid() and listing_media_form.is_valid():
            listing_create_form.instance.listing_status = 'A'
            listing_create_form.instance.created_by = request.user
            form = listing_create_form.save()
            form.save()
            new_listing_id = form.pk
            # loop over images to upload multiple
            for image_uploaded in request.FILES.getlist('image'):
                listing_name = f"{listing_create_form.instance.make}_{listing_create_form.instance.model}_{listing_create_form.instance.pk}"
                compressed_image = compress_uploaded_images(image_uploaded, listing_name)
                image_instance = ListingMedia.objects.create(listing=form, image=compressed_image)
                image_instance.save()
            return redirect('boat_listings')
    else:
        listing_create_form = ListingCreateForm()
        listing_media_form = ListingMediaForm()
    context = {'listing_create_form': listing_create_form, 'listing_media_form': listing_media_form}
    return render(request, 'listings/listing_create_form.html', context)


def home(request):
    return render(request, 'listings/index.html')


def compress_uploaded_images(image, listing_name):
    image = Image.open(image)
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=60)
    image_file = InMemoryUploadedFile(image_io, None, f"{listing_name}.jpeg", 'image/jpeg', image_io.tell(), None)
    print(listing_name)
    return image_file

