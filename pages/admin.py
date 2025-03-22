from django.contrib import admin
from .models import Album, AboutSection

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "title", "price")


@admin.register(AboutSection)
class AboutSection(admin.ModelAdmin):
    list_display = ("title", "is_active")