from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_list(request):
    items = MenuItem.objects.all()
    context = {
        'items': items  # Pass items to the template context
    }
    return render(request, 'menu/menu.html', context)