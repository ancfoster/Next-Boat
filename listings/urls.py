from . import views
from django.urls import path

urlpatterns = [
    path('boats/', views.ListingsList.as_view(), name='boat_listings'),
    path('', views.home, name="home"),
]