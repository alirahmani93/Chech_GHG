from django.contrib import admin
from .models import OurUser, Regular, Staff, Supplier
# Register your models here.
admin.site.register(OurUser)
admin.site.register(Regular)
admin.site.register(Staff)
admin.site.register(Supplier)
