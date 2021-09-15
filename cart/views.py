from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart, CartItem


# Create your views here.


# -------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name = 'checkout-step-1.html'


class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    queryset = Cart.objects.all()
    template_name = 'checkout-step-1.html'


class CreateCart(CreateView):
    model = Cart
    template_name = 'checkout-step-1.html'


class Updatecart(UpdateView):
    model = Cart
    template_name = 'checkout-step-1.html'


class DeleteCart(DeleteView):
    model = Cart
    template_name = 'checkout-step-1.html'


##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name = 'checkout-step-1.html'


class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name = 'checkout-step-1.html'


class CreateItemCart(CreateView):
    model = CartItem
    template_name = 'checkout-step-1.html'


class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'checkout-step-1.html'


class DeleteCartItem(DeleteView):
    model = Cart
    template_name = 'checkout-step-1.html'
