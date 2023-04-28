from django.contrib import admin
from .models import UserType


class UserTypeInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = "UserType"


admin.site.register(UserType)

