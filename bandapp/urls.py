from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'bandapp'
urlpatterns = [
    path('merch_search/', views.merch_search, name='merch_search'),
    #path('<slug:album_slug>/', views.album_detail, name='album_detail'),
    path('<slug:slug>/buy_ticket', views.buy_ticket, name='buy_ticket'),
    path('ticket_confirmation/<int:ticket_id>', views.ticket_confirmation, name='ticket_confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)