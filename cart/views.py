from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem


# Create your views here.


# -------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name = 'checkout-step-1.html'
    context_object_name = "cart_detail"



class ListCart(ListView):
    model = Cart
    queryset = Cart.objects.all()
    template_name = 'checkout-step-1.html'
    context_object_name = "cart_list_view"



class CreateCart(CreateView):
    model = Cart
    template_name = 'checkout-step-1.html'
    context_object_name = "cart_create"


class Updatecart(UpdateView):
    model = Cart
    template_name = 'header.html'
    context_object_name = "cart_update"



class DeleteCart(DeleteView):
    model = Cart
    template_name = 'checkout-step-1.html'
    context_object_name = "cart_delete"


##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name = 'checkout-step-1.html'
    context_object_name = "cartitem_detail"


class ListCartItem(ListView):
    model = CartItem
    template_name = 'checkout-step-1.html'
    context_object_name = "cartitem_list"
    queryset = CartItem.objects.all()


class CreateCartItem(CreateView):
    model = CartItem
    template_name = 'checkout-step-1.html'
    context_object_name = "cartitem_create"


class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'checkout-step-1.html'
    context_object_name = "cartitem_update"


class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'checkout-step-1.html'
    context_object_name = "cartitem_delete"
