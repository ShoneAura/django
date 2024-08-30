from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')


class Category(models.Model):
    name = models.CharField(max_length=255)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    products = models.ManyToManyField(Product, through=OrderItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()