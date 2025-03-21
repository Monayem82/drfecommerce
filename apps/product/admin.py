from django.contrib import admin
from . models import *


class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductDetailsInline,
    ]

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductDetails)