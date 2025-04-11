from django.shortcuts import render
from .models import Album, AboutSection
from django.views.generic import ListView



# Create your views here.
def first_view(request):
    return render(request, "base.html")

#def about_view(request):
    return render(request, "pages/about.html")

#def listings_view(request):
    return render(request,  "pages/listings.html")


def index(request, artist=None):
    print(f"********** {artist}")
    if artist != None:
        print(f" *** artist {artist} ****")
        albums = Album.objects.filter(artist=artist)
        return render(request, "pages/listing.html", {"albums": albums})
    else:
        print("**** ELSE *** ")
        albums = Album.objects.filter(artist="Elvis")
        print(f"albums {albums}")
        return render(request, "pages/listings.html", {"albums": albums})

def album_list(request):
    albums = Album.objects.filter(artist="Elvis")
    print(f"albums {albums}")
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

class PostListView(ListView):
    template_name = "pages/listings.html"
    model = Album
    context_object_name = "albums"

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            print("SEARCH TERM:", search)  # Optional debug
            return Album.objects.filter(title__icontains=search).order_by("artist", "title").reverse()
        return Album.objects.all().order_by("artist", "title").reverse()
