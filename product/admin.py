from django.contrib import admin

from .models import Category, Media, Product, Brand


# Register your models here.

@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


# @admin.register(Media)
# class MediaAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass

#########_____________________###########
class Inline(admin.TabularInline):
    model = Media
    extra = 2
@admin.register(Product)
class ProductInlineAdmin(admin.ModelAdmin):
    inlines = [Inline]

#### Use ""modelAdmin.fiedset"" in your admin #########
