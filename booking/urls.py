from django.contrib import admin
from django.urls import path

from .views import book, barberDetail, ListBarbers, display_gallery, list_appointments, ListBarbers_for_bookings

urlpatterns = [
    # path('', home_introduction.home_introduction, name='home'),
    path('book/', book, name='book'),
    path('barbers/', ListBarbers.as_view(), name='barbers'),
    path('barber/<int:pk>', barberDetail.as_view(), name='barber_detail'),
    path('barber/barber-<int:pk>/barber-gallery', display_gallery, name='barber_gallery'),
    path('list-of-appointments/for-barber-<int:pk>', list_appointments, name='appointments_list'),
    path('list-of-barbers-for-bookings/', ListBarbers_for_bookings.as_view(), name='barbers_booking_list'),
]

