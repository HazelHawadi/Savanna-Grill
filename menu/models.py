from django.db import models

# Create your models here.
class MenuItem(models.Model):
    # Field to store the name of the menu item
    name = models.CharField(max_length=100) #limited to 100 characters
    
    # Field to store a description of the menu item
    description = models.TextField()  # the text can be long
    
    # Field to store the price of the menu item
    price = models.DecimalField(max_digits=5, decimal_places=2)  # (e.g., 12.99)
    
    # Field to store an image of the menu item (its optional)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True) 

    category = models.CharField(max_length=50, default='Main')  # e.g., Appetizer, Main Course, Dessert

    # to show the name of the menu item
    def __str__(self):
        return self.name  # returns the name of the menu item