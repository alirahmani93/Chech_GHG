from django.contrib import admin

from .models import Category, Media, Product, Brand, Attribute,Attributekey


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(Attribute)



class Inline(admin.TabularInline):
    model = Attribute
    extra = 1
@admin.register(Attributekey)
class AttributeKeytInlineAdmin(admin.ModelAdmin):
    inlines = [Inline]

#### Use ""modelAdmin.fiedset"" in your admin #########
