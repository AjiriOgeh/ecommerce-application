from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework import serializers

from ecommerce.models import Product


class FindProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['product_name']


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    field = ['product_name', 'price', 'description', 'category', 'image', 'in_stock']


class AddItemToCartSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=10)
    quantity = serializers.IntegerField(max_value=100)


class RemoveFromCartSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=10)


class PlaceOrderSerializer(serializers.Serializer):
    shopping_cart_id = serializers.CharField(max_length=10)
    receiver_number = serializers.CharField(validators=[MaxLengthValidator(11), MinLengthValidator(11)])
    receiver_address = serializers.CharField(max_length=200,default="")
    receiver_name = serializers.CharField(max_length=225,allow_null=False)