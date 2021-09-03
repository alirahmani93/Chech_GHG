from django.urls import path

from .views import check_payment_successful, go_to_gateway_view
urlpatterns = [
    path('check_payment/', check_payment_successful),
    path('go_to_gateway_view/', go_to_gateway_view),
]
