from django.contrib import admin
from .models import Favourites, Listings


@admin.register(Favourites)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("favourite_created_by", "listing",)
