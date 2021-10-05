from django.contrib.auth import get_user_model
from django.db import models

from cart.models import Cart

user = get_user_model()


# Create your models here.
class Shipping(models.Model):  #### Design Pattern Strategy ####
    city_choices = (("Tehran", "Tehran"), ("Shiraz", "Shiraz"), ("Rasht", "Rasht"),)
    post_choices = (("Post Pishtaz", 1), ("TBT", 2), ("peyk motory", 3))

    cart_one2one = models.OneToOneField("Cart", on_delete=models.RESTRICT)
    post_type = models.CharField(max_length=20, choices=post_choices)
    city = models.CharField(max_length=20, choices=city_choices)

    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='addresses')
    zipcode = models.CharField(max_length=16)
    address = models.TextField()


    # cost_cyrt_choices=
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user
