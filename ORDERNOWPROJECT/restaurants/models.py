from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    NIT = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    grammage = models.FloatField()
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/product_images')


class Table(models.Model):
    code = models.CharField(max_length=7)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
