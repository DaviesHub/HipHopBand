from django.db import models

# Create your models here.
class Album(models.model):
    cover_art = models.ImageField(upload_to='band_logos/', blank=True, null=True) 