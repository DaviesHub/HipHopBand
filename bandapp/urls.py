from django.urls import path
from . import views

urlpatterns = [
    path('<slug:album_slug>/', views.album_detail, name='album_detail'),
    path('<slug:tour_slug>/', views.tour_detail, name='tour_detail'),
    path('<slug:member_slug>/', views.member_detail, name='member_detail'),
    path('<slug:merch_slug>/', views.merch_shop, name='merch_shop'),
]