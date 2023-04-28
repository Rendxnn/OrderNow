from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_of_user = models.IntegerField(default=0)  # user -> 0, cashier -> 1, admin -> 2

    def get_type(self):
        return self.type_of_user

