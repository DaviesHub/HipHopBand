from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('home/', views.home, name='home'),
    path('albums/', views.albums, name='albums'),
    path('tours/', views.tours, name='tours'),
    path('merch/', views.merch_shop, name='merch'),
    path('albums/', views.albums, name='albums'),
    path('contact/', views.contact, name='contact'),
    path('', include('bandapp.urls')),
]