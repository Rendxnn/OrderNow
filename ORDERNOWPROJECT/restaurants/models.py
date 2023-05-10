from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    NIT = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    grammage = models.FloatField()
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/product_images')

    def __str__(self):
        return self.restaurant.__str__() + ' ' + self.name


class Table(models.Model):
    code = models.CharField(max_length=7)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
