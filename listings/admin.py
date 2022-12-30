from django.contrib import admin
from .models import Listings, ListingMedia


@admin.register(ListingMedia)
class ListingMediaAdmin(admin.ModelAdmin):
    list_display = ("listing", "image",)


admin.site.register(Listings)
