from django.urls import path

from .views import address_list, address_create

urlpatterns = [
    path('list/', address_list, name='adress-list'),
    path('create/', address_create, name='adress-creat'),
]
