from django.db import models
from restaurants.models import Table, Product


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.table.__str__() + ' ' + self.product.__str__()


class Observation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.table.__str__()