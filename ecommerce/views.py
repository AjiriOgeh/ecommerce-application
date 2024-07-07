import json

from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import ShoppingCart
from . import serializers
from .models import Customer, Product, Item, Order, BillingInformation


# Create your views here.

def permission():
    permission_classes = [IsAuthenticated]


class FindProductByName(APIView):
    permission()

    @staticmethod
    def get(request):
        serializer = serializers.FindProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.data['product_name']
        products = Product.objects.filter(name=name)
        if products:
            return Response(data=serializers.ProductSerializer(Product, many=True), status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'No Product Of Such Name'}, status=status.HTTP_400_BAD_REQUEST)


class FindProductByCategory(APIView):
    permission()

    @staticmethod
    def get(request):
        serializer = serializers.FindProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_category = serializer.data['product_category']
        products = Product.objects.filter(name=product_category)
        if products:
            return Response(data=serializers.ProductSerializer(products, many=True), status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'No Product Of Such Name'}, status=status.HTTP_400_BAD_REQUEST)


class AddItemToCart(APIView):
    permission()

    @staticmethod
    def post(request):
        user = request.user
        serializer = serializers.AddItemToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)
        item = Item.objects.create(
            quantity=serializer.data['quantity'],
            product=product_id,
            shopping_cart=user.shopping_cart.id
        )

        response = {
            'item_id': item.pk,
            "product": serializers.ProductSerializer(product),
            'quantity': item.quantity,
        }
        return Response(data=response, status=status.HTTP_200_OK)


class RemoveItemFromCart(APIView):
    permission()

    @staticmethod
    def delete(request):
        serializer = serializers.RemoveFromCartSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        item_id = serializer.data['item_id']
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return Response(data={'message': "Deleted"})





class PlaceOrderView(APIView):
    @staticmethod
    def post(request):
        serializer = serializers.PlaceOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shopping_cart = get_object_or_404(ShoppingCart, pk=serializer.data['shopping_cart_id'])
        items = shopping_cart.items
        total_price = sum(map(lambda X: X.price, items))
        BillingInformation.objects.create(
            receiver_name=serializer.data['receiver_name'],
            receiver_address=serializer.data['receiver_address'],
            receiver_number=serializer.data['receiver_number']
        )
        order =Order.objects.create(
            shopping_cart=shopping_cart.id,
            total_price=total_price,
        )
        response ={
            'order_id': order.id
        }
        return Response()
