from django.urls import path
from . import views
from .views import menu_view

urlpatterns=[
    path('', views.menu_view, name='menu_view'),  # Displays all categories
    path('category/<int:id>/', views.category_view, name='category_view'),  # Displays menu items for a specific category
]