from .models import Order, Observation
from restaurants.models import Product, Table


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
    for order in orders:
        if order.table in dic_orders:
            dic_orders[order.table] += [order.product]
        else:
            dic_orders[order.table] = [order.product]
    return dic_orders


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
