from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import Listings, ListingMedia
from django.db.models import Q

# Create your views here.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.filter(Q(listing_status='A') | Q(listing_status='P'))
    template_name = "listings/listings.html"


# class ListingDetails(generic.DetailView):
#     template_name = "listings/listing_details.html"
#     queryset = Listings.objects.all()


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

def home(request):
    return render(request, 'listings/index.html')

