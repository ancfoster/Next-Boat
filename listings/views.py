from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ListingCreateForm, ListingMediaForm
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Listings, ListingMedia
from django.db.models import Q


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
    listing_create_form = ListingCreateForm(request.POST or None, request.FILES)
    listing_media_form = ListingMediaForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if listing_create_form.is_valid() and listing_media_form.is_valid():
            listing_create_form.instance.created_by = request.user
            form = listing_create_form.save()
            form.save()
            new_listing_id = form.pk

            # loop over images to upload multiple
            for image_uploaded in request.FILES.getlist('image'):
                image_instance = ListingMedia.objects.create(listing=form, image=image_uploaded)
                image_instance.save()
            return redirect('boat_listings')
    template = 'listings/listing_create_form.html'
    context = {
        'listing_create_form': listing_create_form,
        'listing_media_form': listing_media_form,
    }
    return render(request, template, context)


def home(request):
    return render(request, 'listings/index.html')

