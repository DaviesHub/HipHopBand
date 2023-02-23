from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Album, Tour, Merch, Ticket, TrackList, Track

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

# def album_details(request, album_slug):
#     album = get_object_or_404(Album, slug=album_slug)

#     return render(request, 'bandapp/album_detail.html', {'album': album})

def tracklist(request, album_slug):
    if request.user.is_authenticated:
        album = get_object_or_404(Album, slug=album_slug)
        tracklist = get_object_or_404(TrackList, album=album)
        tracks = Track.objects.filter(tracklist=tracklist)

        return render(request, 'bandapp/tracklist.html', {'album': album, 'tracks': tracks})
    else:
        return HttpResponseRedirect (
            reverse('user_auth:user_login') 
        )

def tours(request):
    if request.user.is_authenticated:
        tour_list = Tour.objects.order_by('-tour_date')[:]
        context = {'tour_list': tour_list,}

        return render(request, "bandapp/tours.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def buy_ticket(request, slug):
    if request.user.is_authenticated:
        tour = get_object_or_404(Tour, slug=slug)
        tour_list = Tour.objects.order_by('-tour_date')[:]
        context = {'tour_list': tour_list,}
        if request.method == 'POST':
            try:
                quantity = int(request.POST['quantity'])
                if quantity <= 0:
                    raise ValueError(messages.error(request, 'Invalid number of tickets. Enter a positive number of tickets'))
            except (ValueError):
                return render(request, 'bandapp/tours.html', context)
            else:
                ticket = Ticket.objects.create(tour=tour, user=request.user, quantity=quantity)
                ticket.save()
                return HttpResponseRedirect(
                    reverse('bandapp:ticket_confirmation', args=[ticket.id])
                )
        else:
            return render(request, 'bandapp/tours.html', {'tour': tour})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login') 
        )

def ticket_confirmation(request, ticket_id):
    if request.user.is_authenticated:
        ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
        tour = ticket.tour

        return render(request, 'bandapp/ticket_confirmation.html', {'ticket': ticket, 'tour': tour})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def merch_shop(request):
    if request.user.is_authenticated:
        merch_list = Merch.objects.all()
        context = {'merch_list': merch_list}

        return render(request, 'bandapp/merch.html', context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def merch_search(request):
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        merch_list = Merch.objects.filter(Q(merch_description__icontains=query) | Q(merch_name__icontains=query))

        return render(request, 'bandapp/merch_search.html', {'merch_list': merch_list, 'query': query})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

