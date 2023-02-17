from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Album, Tour, Merch, Ticket

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

def tours(request):
    if request.user.is_authenticated:
        tour_list = Tour.objects.order_by('-tour_date')[:1]
        context = {'tour_list': tour_list,}

        return render(request, "bandapp/tours.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def album_detail(request, album_slug):
    album = get_object_or_404(Album, slug=album_slug)

    return render(request, 'bandapp/album_detail.html', {'album': album})

def tour_detail(request, tour_id, tour_slug):
    if request.user.is_autheticated:
        tour = get_object_or_404(Tour, pk=tour_id, slug=tour_slug)
        if request.method == 'POST':
            quantity = int(request.POST['quantity'])
            ticket = Ticket(tour=tour, user=request.user, quantity=quantity)
            ticket.save()

            return render(request, 'bandapp/ticket_confirmation.html')
        else:
            return render(request, 'bandapp/tour_detail.html', {'tour': tour})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def ticket_confirmation(request, tour_id):
    if request.user.is_authenticated:
        tour = get_object_or_404(Tour, pk=tour_id)
        tickets = Ticket.objects.filter(tour=tour)
        total_tickets = tickets.aggregate(Sum('quantity'))['quantity__sum']

        return render(request, 'ticket_confirmation.html', {'tour': tour, 'total_tickets': total_tickets})
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

