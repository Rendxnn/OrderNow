from django.shortcuts import render
from restaurants import restaurants


def home(request):
    table_code = request.GET.get('table_code')
    if table_code:
        table = restaurants.search_table(table_code)
        if table:
            restaurant = table.restaurant
            products = restaurant.product_set.all()
            return render(request, 'menu.html', {'table': table, 'restaurant': restaurant, 'products': products})
    return render(request, 'home.html', {'table_code': table_code})
