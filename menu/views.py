from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_view(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'categories': categories})