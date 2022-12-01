from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Listings
from django.db.models import Q

# Create your views here.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.filter(Q(listing_status='A') | Q(listing_status='P'))
    template_name = "listings/listings.html"


def home(request):
    return render(request, 'listings/index.html')

