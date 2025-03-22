from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to= "media/images/albums/")

    def __str__(self):
        return f"{self.artist} - {self.title}"
    

class AboutSection(models.Model):
    title = models.CharField(max_length=120, default="About Us")
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
