from django.shortcuts import render

# Create your views here.
def menu_list(request):
    return render(request, 'menu/menu.html')