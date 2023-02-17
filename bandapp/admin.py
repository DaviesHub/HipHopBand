from django.contrib import admin
from .models import Album, TrackList, Tour, Merch, Ticket

class TourAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tour_name',)}

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(TrackList)
admin.site.register(Tour, TourAdmin)
admin.site.register(Merch)
admin.site.register(Ticket)