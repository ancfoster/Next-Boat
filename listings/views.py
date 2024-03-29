from django.shortcuts import render, get_object_or_404, redirect
from django.conf.urls import handler404, handler500
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from PIL import Image
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import Listings, ListingMedia
from favourites.models import Favourites
from .forms import ListingCreateForm, ListingMediaForm, ListingEditForm


# Create your views here.
# This view outputs the boats listings with a status of available or pending.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.filter(Q(listing_status='A') | Q(listing_status='P'))  # noqa
    template_name = "listings/listings.html"


# This view shows a user any listings they have on the My Listings page
class MyListings(LoginRequiredMixin, generic.ListView):
    model = Listings
    template_name = 'listings/my_listings.html'

    def get_queryset(self):
        return Listings.objects.filter(created_by=self.request.user)


# This view shows a detailed view of a particular boat
class ListingDetails(View):
    def get(self, request, id, *args, **kwargs):
        queryset = Listings.objects.all()
        listing = get_object_or_404(queryset, id=id)
        listing_favourite = {}
        if request.user.is_authenticated:
            listing_favourite = Favourites.objects.filter(Q(favourite_created_by=request.user) & Q(listing=listing))  # noqa

        gallery_images = listing.listing_media.all()
        preview_images = listing.listing_media.all()[:4]
        return render(
            request,
            "listings/listing_details.html",
            {
                "listing": listing,
                "gallery_images": gallery_images,
                "preview_images": preview_images,
                "listing_favourite": listing_favourite,
            },
        )


# This view deletes a user's listing
class ListingDelete(LoginRequiredMixin, DeleteView):
    template_name = 'listings/listing_delete.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Listings, id=id)

    def get_success_url(self):
        return reverse('my_listings')


# This view creates a new listing
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
            info_string = f"{getMake}-{getModel}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}"  # noqa
            compressed_featured_image = compress_featured_image(featured_image)
            listing_create_form.instance.featured_image = compressed_featured_image  # noqa
            listing_create_form.instance.featured_image.field.upload_to = info_string+'/'  # noqa
            form = listing_create_form.save()
            form.save()
            new_listing_id = form.pk
            # loop over images to  upload multiple
            for image_uploaded in request.FILES.getlist('image'):
                listing_name = f"{listing_create_form.instance.make}_{listing_create_form.instance.model}_{listing_create_form.instance.pk}"  # noqa
                compressed_image = compress_uploaded_images(image_uploaded, listing_name)  # noqa
                image_instance = ListingMedia.objects.create(listing=form, image=compressed_image)  # noqa
                image_instance.image.field.upload_to = info_string+'/'
                image_instance.save()
            return redirect('my_listings')
    else:
        listing_create_form = ListingCreateForm()
        listing_media_form = ListingMediaForm()
    context = {'listing_create_form': listing_create_form, 'listing_media_form': listing_media_form}  # noqa
    return render(request, 'listings/listing_create_form.html', context)


# This view allows a user to edit the details of a listing
@login_required
def EditListing(request, id):
    listing_object = get_object_or_404(Listings, pk=id)
    listing_edit_form = ListingEditForm(request.POST, instance=listing_object)
    if listing_edit_form.is_valid():
        listing_edit_form.save()
        return redirect('my_listings')
    else:
        listing_edit_form = ListingEditForm(instance=listing_object)
    context = {'listing_edit_form': listing_edit_form, 'listing_object': listing_object}  # noqa
    return render(request, 'listings/listing_edit.html', context)

# This view allows a user to upload additional images or start
# the process to delete them


@login_required
def EditImages(request, id):
    listing_media_form = ListingMediaForm(request.POST, request.FILES, )
    listing = get_object_or_404(Listings, pk=id)
    listing_images = listing.listing_media.all()
    if listing_media_form.is_valid():
        for image_uploaded in request.FILES.getlist('image'):
            listing_name = f"{listing.make}_{listing.model}_{listing.pk}"
            compressed_image = compress_uploaded_images(image_uploaded, listing_name)  # noqa
            image_instance = ListingMedia.objects.create(listing=listing, image=compressed_image)  # noqa
            now = datetime.now()
            info_string = f"{listing.make}-{listing.model}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}"  # noqa
            image_instance.image.field.upload_to = info_string+'/'
            image_instance.save()
        return redirect(request.path)
    context = {'listing': listing, 'listing_images': listing_images, 'listing_media_form': listing_media_form}  # noqa
    return render(request, 'listings/listing_edit_images.html', context)


# This view deletes an image
class DeleteImage(LoginRequiredMixin, DeleteView):
    template_name = 'listings/delete_image.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(ListingMedia, pk=id)

    def get_success_url(self):
        id = self.kwargs.get("id")
        listing_image = get_object_or_404(ListingMedia, pk=id)
        listing_pk = listing_image.listing.pk
        return reverse('listing_images', kwargs={'id': self.object.listing.pk})


# This view renders the home page
def home(request):
    return render(request, 'listings/index.html')


# These functions take an image and string as an argument,
# and then compress the image using PILLOW library
# PNGs with alpha channel are converted from 'RGBA' to 'RGB'
def compress_uploaded_images(image, listing_name):
    image = Image.open(image)
    # Code snippet by Prahlad Yeri
    if image.mode in ("RGBA", "P"):
        image = image.convert('RGB')
    # .thumbnail method resizes the uploaded images, values are max height & width  # noqa
    image.thumbnail((1024, 1024))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=70)
    # listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, f"{listing_name}.jpeg", 'image/jpeg', image_io.tell(), None)  # noqa
    return image_file


def compress_featured_image(image):
    image = Image.open(image)
    # Code snippet by Prahlad Yeri
    if image.mode in ("RGBA", "P"):
        image = image.convert('RGB')
    # .thumbnail method resizes the uploaded images, values are max height & width  # noqa
    image.thumbnail((1024, 1024))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=65)
    # listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, 'featured_image.jpeg', 'image/jpeg', image_io.tell(), None)  # noqa
    return image_file
