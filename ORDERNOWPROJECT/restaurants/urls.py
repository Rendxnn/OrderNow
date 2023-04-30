from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('cashier/', views.cashier, name='cashier'),
]



