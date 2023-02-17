from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    cover_art = models.ImageField(upload_to='band_logos/', blank=True, null=True)
    release_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-release_date',)

    def __str__(self):
        return self.title

class TrackList(models.Model):
    album_title = models.ForeignKey(Album, related_name='track_list', on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    track_id = models.IntegerField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Tracklist'

    def __str__(self):
        return self.album_title

class Tour(models.Model):
    tour_name = models.CharField(max_length=100)
    tour_date = models.DateTimeField()
    tour_location = models.CharField(max_length=255)
    tour_image = models.ImageField(upload_to='tour_photos/', blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-tour_date',)

    def __str__(self):
        return self.tour_name

class Ticket(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} tickets for {self.tour.name} ({self.user.username})"

class Merch(models.Model):
    merch_photo = models.ImageField(upload_to='merch_photos/', blank=True, null=True)
    merch_name = models.CharField(max_length=255)
    merch_description = models.TextField(blank=True)
    merch_price = models.DecimalField(max_digits=6, decimal_places=1)

    class Meta:
        verbose_name_plural = 'Merch'

    def __str__(self):
        return self.merch_name
