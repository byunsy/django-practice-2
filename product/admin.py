from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'stock', 'registered_dttm')


admin.site.register(Product, ProductAdmin)
