from django.contrib import admin
from .models import Album, TrackList, Tour, Members, Merch

# Register your models here.
admin.site.register(Album)
admin.site.register(TrackList)
admin.site.register(Tour)
admin.site.register(Members)
admin.site.register(Merch)