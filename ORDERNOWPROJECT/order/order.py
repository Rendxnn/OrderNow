from .models import Order, Observation, DispatchedOrder
from restaurants.models import Product, Table
from datetime import date


def add(product, quantity, table):
    for i in range(int(quantity)):
        order = Order(table=table, product=product)
        order.save()


def search_table_orders(restaurant, table):
    if not table:
        restaurant_tables = Table.objects.all().filter(restaurant=restaurant)
    else:
        restaurant_tables = [table]
    orders = [order for order in Order.objects.all() if order.table in restaurant_tables]
    dic_orders = {}
    dic_totals = {}
    for order in orders:
        if order.table in dic_orders:
            dic_orders[order.table] += [order.product]
            dic_totals[order.table] += order.product.price
        else:
            dic_orders[order.table] = [order.product]
            dic_totals[order.table] = order.product.price
    for total in dic_totals:
        dic_totals[total] = f'{dic_totals[total]:,}'
    return dic_orders, dic_totals


def delete_product_from_order(table, button_name):
    table_orders = Order.objects.all().filter(table=table)
    for order in table_orders:
        if order.product.name == button_name:
            order.delete()
            return


def add_observation(table, description):
    observation = Observation(table=table, description=description)
    observation.save()


def search_table_observations(restaurant, table):
    if not table:
        restaurant_tables = Table.objects.all().filter(restaurant=restaurant)
    else:
        restaurant_tables = [table]
    observations = [observation for observation in Observation.objects.all() if observation.table in restaurant_tables]
    dic_observations = {}
    for observation in observations:
        if observation.table in dic_observations:
            dic_observations[observation.table] += [observation.description]
        else:
            dic_observations[observation.table] = [observation.description]
    return dic_observations


def delete_table_order(table_id):
    table = Table.objects.all().filter(id=table_id)[0]
    orders = Order.objects.all().filter(table=table)
    observations = Observation.objects.all().filter(table=table)
    for order in orders:
        dispatched = DispatchedOrder(table=table, date=date.today(), paid=False, product=order.product)
        dispatched.save()
        order.delete()
    for observation in observations:
        observation.delete()


def search_dispatched_pending(table):
    unpaid = DispatchedOrder.objects.all().filter(table=table, paid=False)
    total_unpaid = sum([dispatched.product.price for dispatched in unpaid])
    return unpaid, f'{total_unpaid:,}'
