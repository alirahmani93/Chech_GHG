from django.urls import path

from .views import  payment_return, payment_start , payment_check

urlpatterns = [



    path('payment', payment_start, name='payment_start'),
    path('payment/return', payment_return, name='payment_return'),
    path('payment/check/<pk>', payment_check, name='payment_check'),

]
