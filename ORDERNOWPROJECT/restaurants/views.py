from django.shortcuts import render, redirect
from order import order
from . import restaurants

table = None
restaurant = None
products = []


def menu(request):
    product_inputs = [request.GET.get(f'{product.name}') for product in products]
    for i in range(len(product_inputs)):
        if product_inputs[i] and product_inputs[i].lower() != 'cantidad de producto':
            order.add(products[i], product_inputs[i], table)
    active_orders = order.search_table_orders(restaurant, table)
    delete_buttons = []
    for current_order in active_orders.values():
        for product_order in current_order:
            delete_buttons.append(request.GET.get(f'delete_{product_order.id}'))
    for i in range(len(delete_buttons)):
        if delete_buttons[i] == '':
            order.delete_product_from_order(table, list(active_orders.values())[0][i].name)
            break
    active_orders = order.search_table_orders(restaurant, table)
    observations = request.GET.get('observations')
    if observations:
        order.add_observation(table, observations)
    return render(request, 'menu.html',
                  {'table': table, 'restaurant': restaurant, 'products': products, 'numbers': range(1, 11),
                   'orders': active_orders.items(), 'observations': observations})


def cashier(request):
    orders = order.search_table_orders(restaurant, None)
    observations = order.search_table_observations(restaurant, None)
    return render(request, 'cashier.html',
                  {'restaurant': restaurant, 'orders': orders.items(), 'observations': observations.items()})
