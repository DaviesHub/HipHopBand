from django.db import models

# Create your models here.
class Album(models.model):
    title = models.CharField(max_length=255)
    cover_art = models.ImageField(upload_to='band_logos/', blank=True, null=True)
    release_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-release_date')

    def __str__(self):
        return self.title

class TrackList(models.Model):
    album = models.ForeignKey(Album, related_name='track_list', on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    track_id = models.IntegerField()
    slug = models.SlugField()

class Tour(models.model):
    tour_name = models.CharField(max_length=100)
    tour_date = models.DateTimeField()
    tour_location = models.CharField(max_length=255)
    slug = models.SlugField()

class Members(models.model):
    member_photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    member_name = models.CharField(max_length=100)
    slug = models.SlugField()
