from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Album, Tour, Members, Merch

# Create your views here.
def albums(request):
    if request.user.is_authenticated:
        album_list = Album.objects.order_by('-release_date')
        context = {'album_list': album_list,}

        return render(request, "bandapp/albums.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def album_detail(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)

    return render(request, 'bandapp/album_detail.html', {'album': album})

def tour_detail(request, tour_slug):
    tour = get_object_or_404(Tour, slug=tour_slug)

    return render(request, 'bandapp/album_detail.html', {'tour': tour})

def member_detail(request, member_slug):
    member = get_object_or_404(Members, slug=member_slug)

    return render(request, 'bandapp/member_detail.html', {'member': member})

def merch_shop(request, merch_slug):
    merch = get_object_or_404(Merch, slug=merch_slug)

    return render(request, 'bandapp/merch_detail.html', {'merch': merch})