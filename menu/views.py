from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_view(request):
    items = MenuItem.objects.all()  # Retrieve all menu items from the database
    return render(request, 'menu/menu.html', {'items': items})