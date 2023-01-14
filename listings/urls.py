from . import views
from django.urls import path

urlpatterns = [
    path('boats/', views.ListingsList.as_view(), name='boat_listings'),
    path('boats/<id>', views.ListingDetails.as_view(), name='boat_listing_details'),
    path('my-listings/', views.MyListings.as_view(), name='my_listings'),
    path('', views.home, name="home"),
    path('create/', views.createListing, name='listing_create'),
]