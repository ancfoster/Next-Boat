from . import views
from django.urls import path

urlpatterns = [
    path('favourite/<id>', views.CreateDeleteFavourite, name='favourite_toggle'),
]