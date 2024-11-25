from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})