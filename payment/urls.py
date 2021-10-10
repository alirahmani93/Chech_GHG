from django.urls import path, include

from rest_framework.routers import SimpleRouter

# from .views import payment_return, payment_start, payment_check
from .api.api_view import PaymentSerializerView,PaymentViewset

simple_router = SimpleRouter()
simple_router.register("payment", PaymentViewset, basename="payment")

urlpatterns = [
    # path('payment', payment_start, name='payment_start'),
    # path('payment/return', payment_return, name='payment_return'),
    # path('payment/check/<pk>', payment_check, name='payment_check'),

    path("api/",include(simple_router.urls)),

]
