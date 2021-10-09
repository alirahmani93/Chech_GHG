from django.db import models

from json import loads , dumps

from product.models import Product
from cart.models import Cart,CartItem
# from shipping.models import Shipping
from users.models import OurUser

# Create your models here.

# class Payment(models.Model):
#     shiping_fk = None
#     shipping_fk = models.ForeignKey("Shipping", on_delete=models.CASCADE, null=True, blank=True)
#     status = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.shiping_fk} , {self.status}"

class Invoice(models.Model):
    user = models.ForeignKey(OurUser, on_delete=models.PROTECT, related_name="invoce", blank=True, null=True)
    m2m = models.ManyToManyField(CartItem, blank=True)

    order_id = models.TextField()
    payment_id = models.TextField()
    amount = models.IntegerField()
    date = models.TextField(default='-')

    card_number = models.TextField(default="****")
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)

    status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk}  |  {self.order_id}  |  {self.status}"


########$$$ MEHRDAD $$$###########
# class Payment(models.Model):
#     shiping_fk = None
#     shipping_fk = models.ForeignKey("Shipping", on_delete=models.CASCADE, null=True, blank=True)
#     status = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.shiping_fk} , {self.status}"
#
# class Invoice(models.Model):
#     user = models.ForeignKey(OurUser,on_delete=models.PROTECT,related_name="invoce",blank=True,null=True)
#     m2m = models.ManyToManyField(CartItem,blank=True)
#
#     # invoice_invoice =models.
#
#
#
# class Main(models.Model):
#
#     order_id = models.TextField()
#     payment_id = models.TextField()
#     amount = models.IntegerField()
#     date = models.TextField(default='-')
#
#     card_number = models.TextField(default="****")
#     idpay_track_id = models.IntegerField(default=0000)
#     bank_track_id = models.TextField(default=0000)
#
#     status = models.IntegerField(default=0)
#
#     def __str__(self):
#         return str(self.pk) + "  |  " + self.order_id + "  |  " + str(self.status)
