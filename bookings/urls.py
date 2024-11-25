from django.urls import path
from . import views

urlpatterns = [
      path('', views.booking_form, name='booking_form'),
    path('booking_success/', views.booking_success, name='booking_success'),  # Success page URL
]