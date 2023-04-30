from .models import Table, Product, Restaurant


def search_table(table_code):
    try:
        table = Table.objects.get(code=table_code)
    except:
        table = None
    return table


def search_product(product_name, restaurant):
    product = Product.objects.all().filter(name=product_name, restaurant=restaurant)
    return product
