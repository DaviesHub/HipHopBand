from django.shortcuts import render, get_object_or_404

from .models import Album

# Create your views here.
def album_detail(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)