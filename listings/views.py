from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Listings

# Create your views here.
class ListingsList(generic.ListView):
    model = Listings
    queryset = Listings.objects.all()
    template_name = "listings/listings.html"


