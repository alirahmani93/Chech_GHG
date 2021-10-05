from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import AddToCartForm
from .models import Cart, CartItem


# @require_POST
def add_to_cart(request):
    response = HttpResponseRedirect(request.POST.get('next', 'home_page'))

    cart = Cart.get_cart(request.COOKIES.get('cart_id', None))
    if Cart is None:
        raise Http404

    response.set_cookie('cart_id', cart.id)

    if not cart.validate_user(request.user):
        raise Http404

    form = AddToCartForm(request.POST)
    if form.is_valid():
        product = form.cleaned_data.get('product')
        quantity = form.cleaned_data.get('quantity')
        form.save(cart=cart)

    # return response
    return redirect("home_page")


@login_required()
def delete_from_cart(request):
    response = HttpResponseRedirect(request.POST.get('next', 'home_page'))
    cart = Cart.get_cart(request.COOKIES.get('cart_id', None)).delete()
    return response


@login_required()
def checkout_step1(request):
    c_item = Cart.get_cart(request.COOKIES.get('cart_id', None))
    t_price = 0
    #
    ############cart_items should be add as  many to many in invoice##
    #
    # for ele in c_item.filter(status='pending'):
    #     t_price += ele.total_price_product
    # context = {
    #     'cart_items': c_item,
    #     'payable': t_price
    # }
    # return render(request, 'checkout-step-1.html', context)
    return render(request, 'checkout-step-1.html', )


#
# # -------------- Cart Views --------------------------------------
# class DetailCart(DetailView):
#     model = Cart
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cart_detail"
#
#
#
# class ListCart(ListView):
#     model = Cart
#     queryset = Cart.objects.all()
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cart_list_view"
#
#
#
# class CreateCart(CreateView):
#     model = Cart
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cart_create"
#
#
class Updatecart(UpdateView):
    model = Cart
    template_name = 'header.html'
    context_object_name = "cart_update"

#
#
# class DeleteCart(DeleteView):
#     model = Cart
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cart_delete"
#
#
# ##-------------- CartItem Views --------------------------------------
# class DetailCartItem(DetailView):
#     model = CartItem
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cartitem_detail"
#
#
# class ListCartItem(ListView):
#     model = CartItem
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cartitem_list"
#     queryset = CartItem.objects.all()
#
#
# class CreateCartItem(CreateView):
#     model = CartItem
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cartitem_create"
#
#
# class UpdateCartItem(UpdateView):
#     model = CartItem
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cartitem_update"
#
#
# class DeleteCartItem(DeleteView):
#     model = Cart
#     template_name = 'checkout-step-1.html'
#     context_object_name = "cartitem_delete"
