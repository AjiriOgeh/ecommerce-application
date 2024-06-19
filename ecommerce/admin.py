from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'image', 'price', 'in_stock']
    search_fields = ['name', 'product_category']

