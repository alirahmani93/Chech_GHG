from django.contrib import admin

from .models import Category, Media, Product, Brand, Attribute


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(Attribute)



# class Inline(admin.TabularInline):
#     model = Media
#     extra = 1
# @admin.register(Product)
# class ProductInlineAdmin(admin.ModelAdmin):
#     inlines = [Inline]

#### Use ""modelAdmin.fiedset"" in your admin #########
