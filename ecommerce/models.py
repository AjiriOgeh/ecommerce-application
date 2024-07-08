from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from ecommerce_application import settings
from user.models import Customer, ShoppingCart


# Create your models here.


class Address(models.Model):
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


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
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2,default=0.00)


class BillingInformation(models.Model):
    receiver_number = models.CharField(max_length=11,validators=[MaxLengthValidator(11), MinLengthValidator(11)],default="")
    receiver_address = models.TextField(blank=False,default="")
    receiver_name = models.CharField( max_length=225,default="")


class Order(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=25, decimal_places=2)
    billing_format = models.ForeignKey(BillingInformation, on_delete=models.PROTECT)
