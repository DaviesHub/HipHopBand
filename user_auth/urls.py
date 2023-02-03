from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('home/', views.home, name='home'),
]