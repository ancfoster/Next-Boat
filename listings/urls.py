from . import views
from django.urls import path

urlpatterns = [
    path('boats/', views.ListingsList.as_view(), name='boat_listings'),
    # path('boats/<pk>', views.ListingDetails.as_view(), name='boat_listing_details'),
    path('boats/<id>', views.ListingDetails.as_view(), name='boat_listing_details'),
    path('', views.home, name="home"),
    path('create/', views.ListingCreate.as_view(), name="listingcreate"),
]