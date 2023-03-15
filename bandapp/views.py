from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Album, Tour, Merch, Ticket, TrackList, Track

# Create your views here.
def albums(request):
    '''
        Renders a list of albums by the hip hop band.

        Args:
            request: A HttpRequest object that contains the album request parameters and user information.

        Returns:
            A HttpResponse object that renders an HTML template with a list of album objects from the database.

        Raises:
            Http404: If the requested album does not exist in the database.
    '''

    if request.user.is_authenticated:
        album_list = Album.objects.order_by('-release_date')
        context = {'album_list': album_list,}

        return render(request, "bandapp/albums.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )


def tracklist(request, album_slug):
    '''
        Renders a list of tracks belonging to an album.

        Args:
            request: A HttpRequest object that contains the track request parameters and user information.
            album_slug: A string that represents the album slug.

        Returns:
            A HttpResponse object that renders an HTML template with a list of an album track objects from the database.

        Raises:
            Http404: If the requested album or track does not exist in the database.
    '''

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
    '''
        Renders a list of available tours by the hip hop band.

        Args:
            request: A HttpRequest object that contains the tour request parameters and user information.

        Returns:
            A HttpResponse object that renders an HTML template with a list of tour objects from the database.

        Raises:
            Http404: If the requested tour does not exist in the database.
    '''

    if request.user.is_authenticated:
        tour_list = Tour.objects.order_by('-tour_date')[:]
        context = {'tour_list': tour_list,}

        return render(request, "bandapp/tours.html", context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )


def buy_ticket(request, slug):
    '''
        Renders a form that enables users choose number of tickets to buy for a tour.

        Args:
            request: A HttpRequest object that contains the tour request parameters and user information.
            slug: A string that represents the unique identifier for a tour object.

        Returns:
            A HttpResponseRedirect object that redirects the user to the ticket confirmation page on successful purchase.
            A rendered HTML template with a list of tours if there was an error in the form submission or the user is not authenticated.

        Raises:
            Http404: If the requested tour does not exist in the database.
    '''

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
    '''
        View function that confirms successful ticket purchase to user.

        Args:
            request: A HttpRequest object that contains the tour and ticket request parameters and user information.
            ticket_id: An integer that represents the unique identifier for a ticket object.

        Returns:
            a page showing the user the number of tickers purchased.

        Raises:
            Http404: If the requested ticket does not exist in the database.
    '''

    if request.user.is_authenticated:
        ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
        tour = ticket.tour

        return render(request, 'bandapp/ticket_confirmation.html', {'ticket': ticket, 'tour': tour})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

def merch_shop(request):
    '''
        Renders a list of merch sold by the hip hop band.

        Args:
            request: A HttpRequest object that contains the merch request parameters and user information.

        Returns:
            A HttpResponse object that renders an HTML template with a list of merch objects from the database.

        Raises:
            Http404: If the requested merch does not exist in the database.
    '''

    if request.user.is_authenticated:
        merch_list = Merch.objects.all()
        context = {'merch_list': merch_list}

        return render(request, 'bandapp/merch.html', context)
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )


def merch_search(request):
    '''
        merch_search function enables authenticated users to search for available merch based on a given query.

        Args:
        request (HttpRequest): An instance of the HttpRequest object that contains metadata about the user's request.

        Returns:
        It returns the rendered template for merch objects that match and query context variables.

        Raises:
        N/A
'''
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        merch_list = Merch.objects.filter(Q(merch_description__icontains=query) | Q(merch_name__icontains=query))

        return render(request, 'bandapp/merch_search.html', {'merch_list': merch_list, 'query': query})
    else:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )


def contact(request):
    '''
        Renders the hip hop band's contacts.

        Args:
            request: A HttpRequest object that contains the request parameters.

        Returns:
            A HttpResponse object that renders an HTML template with the band's contacts.

        Raises:
            N/A
    '''
    return render(request, 'bandapp/contact.html')