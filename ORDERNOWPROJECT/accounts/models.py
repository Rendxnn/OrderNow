from django.db import models
from django.contrib.auth.models import User
from restaurants import models as rest_models


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='type')
    type_of_user = models.IntegerField(default=0)  # user -> 0, cashier -> 1, admin -> 2
    restaurant = models.ForeignKey(rest_models.Restaurant, on_delete=models.CASCADE, null=True, blank=True)

    def get_type(self):
        return self.type_of_user

    def __str__(self):
        return self.user.__str__()
