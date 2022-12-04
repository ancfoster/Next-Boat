from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ListingCreateForm
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
        images = listing.listing_media.all()
        
        return render(
            request,
            "listings/listing_details.html",
            {
                "listing": listing,
                "images": images
            },
        )


class ListingCreate(CreateView):
    model = Listings
    template_name = "listings/listing_create_form.html"
    form_class = ListingCreateForm


class ListingCreate(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ListingCreateForm()}
        return render(request, 'listings/listing_create_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ListingCreateForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()
            return HttpResponseRedirect('')
        return render(request, 'listings/listing_create_form.html', {'form': form})

def home(request):
    return render(request, 'listings/index.html')

