from django.db import models

# Create your models here.
class Booking(models.Model):
    # A field to store the name of the person making the booking
    customer_name = models.CharField(max_length=100)  #limit of 100 characters
    
    # A field to store the date of the booking
    booking_date = models.DateField()
    
    # A field to store the time of the booking
    booking_time = models.TimeField() 
    
    # A field to store the number of guests for the booking
    num_guests = models.PositiveIntegerField()

    # email field
    email = models.EmailField()

    # A method that defines how to show the booking information as a string
    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date} at {self.booking_time}"