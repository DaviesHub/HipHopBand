from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'bandapp'
urlpatterns = [
    path('merch_search/', views.merch_search, name='merch_search'),
    path('<slug:album_slug>/', views.album_detail, name='album_detail'),
    path('<slug:tour_slug>/', views.tour_detail, name='tour_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)