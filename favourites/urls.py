from . import views
from django.urls import path

urlpatterns = [
    path('favourite/<id>', views.CreateDeleteFavourite, name='favourite_toggle'),
    path('favourites/', views.ShowFavourites.as_view(), name='favourites_show'),
]