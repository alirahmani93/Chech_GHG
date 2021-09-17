from django.urls import path

# from .views import DetailCart,ListCart,CreateCart,Updatecart,DeleteCart
from .views import ListCart,DetailCart , CreateCart, Updatecart, DeleteCart
from .views import *


urlpatterns = [
    path('cart-detail/<int:pk>', DetailCart.as_view(), name='cart-detail'),
    path('cart-list/',   ListCart.as_view()  , name='cart-list'),
    path('cart-create/', CreateCart.as_view(), name='cart-create'),
    path('cart-update/<int:pk>', Updatecart.as_view(), name='cart-update'),
    path('cart-delete/<int:pk>', DeleteCart.as_view(), name='cart-delete'),

    path('cartitemcart-detail/<int:pk>', DetailCartItem.as_view(),      name='cartitem-detail'),
    path('cartitem-list/',   ListCartItem.as_view()  ,          name='cartitem-list'),
    path('cartitem-create/', CreateCartItem.as_view(),          name='cartitem-create'),
    path('cartitem-update/<int:pk>', UpdateCartItem.as_view(),  name='cartitem-update'),
    path('cartitem-delete/<int:pk>', DeleteCartItem.as_view(),          name='cartitem-delete'),

]
