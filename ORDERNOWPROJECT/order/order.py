from .models import Order
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
