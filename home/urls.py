from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('about/',views.about,name='about'),
    path('reservations/'views.reservations,name='reservations'),
]
handler404="home.views.custom_404_view"