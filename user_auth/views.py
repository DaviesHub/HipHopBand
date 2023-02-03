from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def login(request):
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

        if password1 == password2:
            messages.error(request, 'Passwords do not match. Enter password again.')
            return render(request, 'authentication/register.html')

        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, 
            username=username,password=password1)
        user.save()

        messages.success(request, 'Your account has been created successfully!')
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )

    return render(request, 'authentication/register.html')