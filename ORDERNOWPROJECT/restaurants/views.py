from django.shortcuts import render, redirect
from order import order
from . import restaurants

table = None
restaurant = None
products = []


def menu(request):
    product_inputs = [request.GET.get(f'{product.name}') for product in products]
    print(product_inputs)
    for i in range(len(product_inputs)):
        if product_inputs[i] and product_inputs[i].lower() != 'cantidad de producto':
            order.add(products[i], product_inputs[i], table)
    return render(request, 'menu.html',
                  {'table': table, 'restaurant': restaurant, 'products': products, 'numbers': range(1, 11)})


def cashier(request):
    orders = order.search_table_orders(restaurant)
    print(type(orders))
    return render(request, 'cashier.html', {'restaurant': restaurant, 'orders': orders.items()})
