from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=200, unique=True)


class Address(models.Model):
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Product(models.Model):
    PRODUCT_TYPE = [
        ('Electronics', 'ELECTRONICS'),
        ('Fashion', 'FASHION'),
        ('Food', 'FOOD'),
        ('Beverages', 'BEVERAGES'),
        ('Furniture', 'FURNITURE'),
        ('Media', 'MEDIA'),
        ('Health', 'HEALTH'),
        ('Books', 'BOOKS'),
        ('Sports', 'SPORTS'),
        ('Toys', 'TOYS')
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    product_category = models.CharField(max_length=20, choices=PRODUCT_TYPE, default='Toys')
    image = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=True)

    # product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class Item(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class BillingInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
