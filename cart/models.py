from django.db import models

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
    user_fk = models.OneToOneField(OurUser, on_delete=models.RESTRICT, null=True, blank=True, related_name='carts')
    # Attributes
    cart_status = models.CharField(max_length=100, choices=status_choices, default=status_choices[0])
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_fk.email}"

    def validate_user(self, user):
        if user.is_authenticated:
            if self.user_fk is not None and self.user_fk != user:
                return False
            if self.user_fk is None:
                self.user_fk = user
                super().save()
        elif self.user_fk is not None:
            return False
        return True

    @classmethod
    def get_cart(cls, cart_id):
        if cart_id is None:
            cart = cls.objects.create()
        else:
            try:
                cart = cls.objects.get(pk=cart_id)
            except cls.DoesNotExist:
                cart = None
        return cart

    def save(self, **kwargs):
        # if not self.user_fk:
        #     raise Exception("bishtar az dota shod ke")
        return super().save()


class CartItem(Log):
    status_choices = (('pending', 'pending'), ('paid', 'paid'), ('None', 'None'))

    # FK
    cart_fk = models.ForeignKey(Cart, on_delete=models.RESTRICT, related_name="cart_fks", null=True, blank=True)
    product_fk = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name="product_fks", null=True,
                                   blank=True)
    # Attrs
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    is_selected = models.BooleanField(default=False)

    def add(self, product, qty=1):
        if self.objects.product_fk.filter(product=product).first():
            product_item = self.product_fk.objects.filter(product=product).first()
            product_item.quantity += qty
            product_item.save()

        else:
            product_item = self.product_fk.objects.create(product=product, quantity=qty)
        return product_item

    @property
    def cond1(self) -> int:
        print("up")
        x = Product.objects.get(id=self.product_fk.id).count
        print(x, self.quantity)

        if x - self.quantity > 0:
            y = x - self.quantity
            y = Product.objects.get(id=self.product_fk.id).count
            print(y)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.product_fk.name}"

#   can have a table for every future invoice
