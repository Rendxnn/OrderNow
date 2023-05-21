import os
from django.conf import settings
from django.http import HttpResponse
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
    active_orders, totals = order.search_table_orders(restaurant, table)
    delete_buttons = []
    for current_order in active_orders.values():
        for product_order in current_order:
            delete_buttons.append(request.GET.get(f'delete_{product_order.id}'))
    for i in range(len(delete_buttons)):
        if delete_buttons[i] == '':
            order.delete_product_from_order(table, list(active_orders.values())[0][i].name)
            break
    active_orders, totals = order.search_table_orders(restaurant, table)
    observations = request.GET.get('observations')
    if observations:
        order.add_observation(table, observations)
    active_observations = order.search_table_observations(restaurant, table)
    unpaid_orders, total_unpaid = order.search_dispatched_pending(table)
    pay_button = request.GET.get('pay_button')
    if pay_button == '':
        order.generate_receipt(restaurant, table, unpaid_orders, total_unpaid)
        order.pay_dispatched_order(table)
        file_path = os.path.join(settings.MEDIA_ROOT, f'receipts/receipt{table.__str__()}.pdf')
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        else:
            return HttpResponse('El archivo no existe.')
    unpaid_orders, total_unpaid = order.search_dispatched_pending(table)
    return render(request, 'menu.html',
                  {'table': table, 'restaurant': restaurant, 'products': products, 'numbers': range(1, 11),
                   'orders': active_orders.items(), 'observations': observations,
                   'active_observations': active_observations.items(), 'totals': totals.items(),
                   'unpaid_orders': unpaid_orders, 'total_unpaid': total_unpaid})


def cashier(request):
    orders, totals = order.search_table_orders(restaurant, None)
    observations = order.search_table_observations(restaurant, None)
    delete_orders = [request.GET.get(f'delete_{table.id}_order') for table in orders.keys()]
    for delete_button in range(len(orders.keys())):
        if delete_orders[delete_button] == '':
            order.delete_table_order(list(orders.keys())[delete_button].id)
    undo_dispatched = request.GET.get('undo_dispatched')
    if undo_dispatched == '':
        order.undo_dispatch(restaurant)
    orders, totals = order.search_table_orders(restaurant, None)
    return render(request, 'cashier.html',
                  {'restaurant': restaurant, 'orders': orders.items(), 'observations': observations.items(),
                   'totals': totals.items()})


def restaurant_admin(request):
    return render(request, 'restaurant_admin.html', {'restaurant': restaurant, 'table_number': range(1, 11)})
