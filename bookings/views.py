from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() # Save the booking to the database
            return redirect('booking_success')  # Redirect after successful booking
    else:
        form = BookingForm()
    return render(request, 'bookings/bookings.html', {'form': form})

# Define the booking_success view
def booking_success(request):
    return render(request, 'booking_success.html')