from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'email', 'booking_date', 'booking_time', 'num_guests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

        # validation for booking date
    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < datetime.date.today():
            raise forms.ValidationError("This booking date is in the past.")
        return booking_date

         #  validation for booking time (restaurant open hours from 10 AM to 10 PM)
    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        if booking_time < datetime.time(10, 0) or booking_time > datetime.time(22, 0):
            raise forms.ValidationError("Booking time must be between 10:00 AM and 10:00 PM.")
        return booking_time