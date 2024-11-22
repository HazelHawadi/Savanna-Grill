from django.urls inport path
from . import views

urlpatterns=[
    path('', views.menu_list, name='menu_list')
]