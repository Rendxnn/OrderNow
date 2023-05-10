from django.contrib import admin
from .models import Order, Observation, DispatchedOrder

admin.site.register(Order)
admin.site.register(Observation)
admin.site.register(DispatchedOrder)

