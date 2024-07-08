from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'image', 'price', 'in_stock']
    search_fields = ['account_number', 'first_name', 'last_name']
    list_editable = ['product_category', 'price']
    list_display_links = ['name']
