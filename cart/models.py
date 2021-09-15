import time

from django.db import models
# from product.models import Product
from django.utils.translation import gettext_lazy as _
from users.models import Regular
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
    user_fk = models.ForeignKey(Regular, on_delete=models.CASCADE, null=True, blank=True)

    # Attrs
    cart_uuid = models.UUIDField("شماره کارت ساخته شده", unique_for_date=1, default=None)
    cart_status = models.CharField(max_length=100, choices=status_choices, default=status_choices[0])
    active = models.BooleanField(default=True)


class CartItem(Log):
    # FK
    cart_fk = models.OneToOneField("Cart", on_delete=models.RESTRICT, null=True, blank=True)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    # Attrs
    quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if (Product.count - self.quantity) > 0:
            Product.count -= self.quantity
        else:
            raise ValueError(f"از این کالا در انبار به تعداد {Product.count} موجود است")

