from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "pages/about.html")

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