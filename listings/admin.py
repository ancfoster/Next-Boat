from django.contrib import admin
from .models import Listings, ListingMedia

# Register your models here.
admin.site.register(Listings)
admin.site.register(ListingMedia)