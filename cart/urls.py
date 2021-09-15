from django.urls import path

# from .views import DetailCart,ListCart,CreateCart,Updatecart,DeleteCart
from .views import ListCart,DetailCart , CreateCart, Updatecart, DeleteCart

urlpatterns = [
    path('cart-detail/', DetailCart.as_view(), name='cart-detail'),
    path('cart-list/',   ListCart.as_view()  , name='cart-list'),
    path('cart-create/', CreateCart.as_view(), name='cart-create'),
    path('cart-update/', Updatecart.as_view(), name='cart-update'),
    path('cart-delete/', DeleteCart.as_view(), name='cart-delete'),

]
