from django.shortcuts import render

# Create your views here.
def booking_form(request):
    return render(request, 'bookings/bookings.html')