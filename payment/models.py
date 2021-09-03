from django.db import models

from json import loads , dumps

from product.models import Product
from cart.models import Cart
from shipping.models import Shipping
# Create your models here.


class Payment(models.Model):
    shiping_fk = None
    shipping_fk = models.ForeignKey("Shipping", on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shiping_fk} , {self.status}"
