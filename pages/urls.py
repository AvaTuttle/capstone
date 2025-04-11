from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about_view, name="about"),
    #path("listings/", views.listings_view, name="listings"),
    path("listings/", views.index, name="album_list"),
    #path("<artist>", views.index, name="album_list")
]