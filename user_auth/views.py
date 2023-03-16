from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from bandapp.views import *


# Create your views here.
def index(request):
    '''
        This function renders the index page for unauthenticated users.

        Args:
            request: A HttpRequest object that contains the request parameters.

        Returns:
            A HttpResponse object that renders an HTML template of the index.

        Raises:
            N/A.
    '''

    return render(request, 'bandapp/index.html')
    
def user_login(request):
    '''
        This function renders the login page for users to log in.

        Args:
            request: A HttpRequest object that contains the request parameters.

        Returns:
            A HttpResponse object that renders an HTML template of the login page.

        Raises:
            N/A.
    '''
    return render(request, 'authentication/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already in use. Choose a different username.')
            return render(request, 'authentication/register.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match. Enter password again.')
            return render(request, 'authentication/register.html')

        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, 
            username=username,password=password1)
        user.save()

        messages.success(request, 'Your account has been created successfully!')
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )

    return render(request, 'authentication/register.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, 'Wrong credentials! Enter details again.')
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:home')
        )

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    return render(request, 'bandapp/home.html', {
        "firstname": request.user.first_name
    })