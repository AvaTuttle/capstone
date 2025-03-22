from django.urls import path
from . import views
from .views import album_list

urlpatterns = [
    path("about/", views.about_view, name="about"),
    #path("listings/", views.listings_view, name="listings"),
    path("listings/", album_list, name="album_list")
]