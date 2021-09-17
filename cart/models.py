import time

from django.db import models
# from product.models import Product
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from product.models import Product
from users.models import Regular, Staff, Supplier, OurUser


# Create your models here.
class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cart(Log):
    status_choices = (('on_cart', 'on_cart'), ('ready_to_pay', 'ready_to_pay'))
    # FK
    user_fk = models.ForeignKey(OurUser, on_delete=models.RESTRICT, null=True, blank=True)
    cart_item = models.ForeignKey("CartItem", on_delete=models.RESTRICT, null=True, blank=True)
    # Attributes
    # cart_uuid = models.UUIDField(verbose_name="شماره کارت ساخته شده", unique_for_date=1, default=None,)
    cart_status = models.CharField(max_length=100, choices=status_choices, default=status_choices[0])
    active = models.BooleanField(default=True)

    def save(self, **kwargs):
        if not self.user_fk:
            raise Exception("bishtar az dota shod ke")
        return super().save()

    def __str__(self):
        return f"{self.user_fk.email}"


class CartItem(Log):
    # FK
    product_fk = models.ForeignKey(Product, on_delete=models.RESTRICT, null=True, blank=True)
    # Attrs
    quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    @property
    def cond1(self) -> int:
        print("2:", Product.count)
        if (Product.count - self.quantity) > 0:
            Product.count -= self.quantity
            print("1:", Product.count)
        return Product.count

    # def save(self, **kwargs):
    #     print("Save")
    #     if self.quantity < 0:
    #         raise Exception("tedad manfi mojaz nist")
    #
    #     super().save()

    def __str__(self):
        return f"{self.product_fk.name}"
