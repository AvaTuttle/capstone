from django.shortcuts import render
from .models import Album, AboutSection


# Create your views here.
def first_view(request):
    return render(request, "base.html")

#def about_view(request):
    return render(request, "pages/about.html")

#def listings_view(request):
    return render(request,  "pages/listings.html")

def album_list(request):
    albums = Album.objects.all()
    return render(request, "pages/listings.html", {"albums": albums})

def about_view(request):
    about_sections = AboutSection.objects.filter(is_active=True)
    return render(request, "pages/about.html", {"about_sections": about_sections})

"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""