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
    '''
        This function allows new users register to the app with given credentials. If request method is POST, extract
        user credentials, verify username and password and create new user. If request methid is not POST, render
        register page.

        Args:
            request: A HttpRequest object representing user request.

        Returns:
            A HttpResponse object with either the register page or a redirect to the user login page, depending on 
            the request method and input data.

        Raises:
            N/A.
    '''

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
    '''
        This function authenticates a user with the given username and password.

        It extracts the username and password from the request's POST data, and authenticates the user with 
        the Django authentication framework's authenticate function. If the authentication fails, return an error
        message and redirect to the user login page. 

        Args:
            request: A HttpRequest object representing the user's request.

        Returns:
            A HttpResponse object with either an error message and redirect to
            the user login page, or a redirect to the home page, depending on the
            authentication result.
    '''

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
    '''
        This function renders the home page for authenticated users.

        Args:
            request: A HttpRequest object that contains the request parameters.

        Returns:
            A HttpResponse object that renders the home page with username of user printed.

        Raises:
            N/A.
    '''

    if not request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('user_auth:user_login')
        )
    return render(request, 'bandapp/home.html', {
        "firstname": request.user.first_name
    })