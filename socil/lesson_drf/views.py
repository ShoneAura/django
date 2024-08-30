from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView

from lesson_drf.models import Product, Category, Order, OrderItem
from lesson_drf.serializer import ProductSerializer, CategorySerializer, UserSerializer, OrderSerializer, \
    AddressSerializer


class DRFView(APIView):
    def get(self, request):
        category = Category.objects.filter(name='Electronics').first()

        data = {
            'name': 'Smartphone',
            'price': '800.00',
            'description': 'A smartphone with the latest features.',
            'category_id': category.id
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()
            print(product.id)

        product = Product.objects.all().last()
        serializer = ProductSerializer(product)
        print(serializer.data)

        data = {
            'street': '123 Main St',
            'city': 'New York',
            'country': 'USA'
        }
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            address = serializer.save()
        else:
            print(serializer.errors)

        data = {
            'street': 'Красная площадь',
            'city': 'Москва',
            'country': 'Russia'
        }
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            address = serializer.save()
            print(address.id)