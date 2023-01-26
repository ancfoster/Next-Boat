from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from datetime import datetime
from .models import Favourites
from listings.models import Listings


# This view crates a favourite but also deletes
# The favourite button in a listing acts as a toggle button
@login_required
def CreateDeleteFavourite(request, id):
    listing_object = get_object_or_404(Listings, pk=id)
    existing_favourite = Favourites.objects.filter(Q(favourite_created_by=request.user) & Q(listing=listing_object.pk))
    if existing_favourite.exists():
        existing_favourite.delete()
        return redirect('boat_listing_details', id=id)
    else:
        new_favourite = Favourites(
            favourite_created_by = request.user,
            listing = listing_object
        )
        new_favourite.save()
        return redirect('boat_listing_details', id=id)
    return render(request, 'favourites/favourite_toggle.html')


# This view shows a user any boats htye have favourited
class ShowFavourites(LoginRequiredMixin, generic.ListView):
    model = Favourites
    template_name = 'favourites/favourites.html'
    def get_queryset(self):
        return Favourites.objects.filter(favourite_created_by=self.request.user)


#This view deletes a user's listing from the favourites list
class FavouriteDelete(LoginRequiredMixin, DeleteView):
    template_name = 'favourites/favourite_delete.html'
    def get_object(self):
        id= self.kwargs.get("id")
        return get_object_or_404(Favourites, id=id)

    def get_success_url(self):
        return reverse('favourites_show')
