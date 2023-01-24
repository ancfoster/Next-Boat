from . import views
from django.urls import path

urlpatterns = [
    path('boats/', views.ListingsList.as_view(), name='boat_listings'),
    path('boats/<id>', views.ListingDetails.as_view(), name='boat_listing_details'),
    path('boats/<id>/delete', views.ListingDelete.as_view(), name='listing_delete'),
    path('boats/<id>/edit', views.EditListing, name='listing_edit'),
    path('my-listings/', views.MyListings.as_view(), name='my_listings'),
    path('', views.home, name="home"),
    path('create/', views.createListing, name='listing_create'),
]

handler404 = 'listings.views.view404'