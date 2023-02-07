from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('<slug:album_slug>/', views.album_detail, name='album_detail'),
]