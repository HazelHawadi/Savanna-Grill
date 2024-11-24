from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_form, name='booking_form'), # Links to the `booking_form` view
]