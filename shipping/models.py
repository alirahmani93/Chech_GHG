from django.db import models


# from cart.models import Cart
# Create your models here.
class Shipping(models.Model):
    city_choices = (("Tehran", "Tehran"), ("Shiraz", "Shiraz"), ("Rasht", "Rasht"),)
    post_choices = (("Post Pishtaz", 1), ("TBT", 2), ("peyk motory", 3))

    # cart_one2one = models.OneToOneField("Cart", on_delete=models.RESTRICT)
    post_type = models.CharField(max_length=20, choices=post_choices)
    city = models.CharField(max_length=20, choices=city_choices)
    # cost_cyrt_choices=
    status = models.BooleanField(default=False)

