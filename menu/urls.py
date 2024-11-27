from django.urls import path
from . import views
from .views import menu_view

urlpatterns=[
    path('', menu_view, name='menu'),
    path('category/<int:id>/', views.category_view, name='category_view'),
]