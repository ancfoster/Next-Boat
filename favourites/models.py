from django.db import models
from listings.models import Listings
from django.contrib.auth.models import User


# Create your models here.
class Favourites(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='favourite_listing')
    
    def __str__(self):
        return f"{self.listing}"
