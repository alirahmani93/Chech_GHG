from django import forms

from product.models import Product


class AddToCartForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)
    quantity = forms.IntegerField(
        )

    def save(self, cart):
        # cart.add(
        #     self.cleaned_data.get('product'),
        #     self.cleaned_data.get('quantity')
        # )
        return cart
