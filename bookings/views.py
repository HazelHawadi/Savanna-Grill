from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() # Save the booking to the database
            return redirect(request, 'bookings/booking_success.html')  # Redirect after successful booking
    else:
        form = BookingForm()
    return render(request, 'bookings/bookings.html', {'form': form})