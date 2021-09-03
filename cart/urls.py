from django.urls import path

from .views import generate_cart
urlpatterns = [
    path('generate_cart/', generate_cart),

]
