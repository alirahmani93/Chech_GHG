from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save

from product.models import Product
from .models import CartItem

# @receiver(pre_save, sender=CartItem)
# def create_CartItem(sender, instance, created,**kwargs):
#     if created:
#         try:
#             Product.objects.create(user=instance)
#
#         except:
#             instance.delete()

