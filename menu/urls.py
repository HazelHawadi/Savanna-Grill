from django.urls import path
from .views import menu_list

urlpatterns=[
    path('menu/', menu_view, name='menu')
]