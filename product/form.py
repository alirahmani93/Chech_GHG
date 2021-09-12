from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_upc(self):
        data = self.cleaned_data['upc']

        if len(str(data)) != 12:
            raise ValidationError(
                f'Invalid value: {data}',
                code='invalid',
            )

        if not data.is_digit:
            raise ValidationError(
                f'Invalid type: {data}',
                code='invalid',
            )
        return data

