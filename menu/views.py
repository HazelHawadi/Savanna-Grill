from django.shortcuts import render
from .models import Category, MenuItem

# Create your views here.
# View for displaying all categories
def menu_view(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'categories': categories})

# View for displaying menu items in a specific category
def category_view(request, id):
    category = get_object_or_404(Category, id=id)  # Get the category by id
    menu_items = MenuItem.objects.filter(category=category)  # Filter items by category
    return render(request, 'menu/category_detail.html', {'category': category, 'menu_items': menu_items})