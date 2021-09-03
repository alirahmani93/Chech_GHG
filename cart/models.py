from django.db import models
# from product.models import Product
from django.utils.translation import gettext_lazy as _
from users.models import Regular
from product.models import Product

# Create your models here.

class Cart(models.Model):
    status_choices = (('on_cart', 'on_cart'), ('ready_to_pay', 'ready_to_pay'))

    cart_uuid= models.UUIDField("شماره کارتی ساخته شده",unique_for_date=1,default=None)
    # user_fk = models.ForeignKey("Regular", on_delete=models.CASCADE)
    # product_fk = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)
    cart_status = models.CharField(max_length=100, choices=status_choices, default=None)
    ordered_count = models.IntegerField("تعداد سفارش شده")
    cost_price = Product.cost

    # class Meta:
    #     db_table = 'سبد خرید'

    def __str__(self):
        return self.cart_uuid
