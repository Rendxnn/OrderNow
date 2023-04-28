from django.db import models
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Table(models.Model):
    code = models.CharField(max_length=7)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)

    