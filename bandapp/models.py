from django.db import models

# Create your models here.
class Album(models.model):
    title = models.CharField(max_length=255)
    cover_art = models.ImageField(upload_to='band_logos/', blank=True, null=True)
    release_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-release_date')

    def __str__(self):
        return self.title