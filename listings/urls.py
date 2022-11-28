from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListingsList.as_view(), name='boat_listings'),
]