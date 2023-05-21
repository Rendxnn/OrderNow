from django.shortcuts import render, redirect
from restaurants import restaurants
from restaurants import views as rest_views


def home(request):
    if request.user.is_authenticated and request.user.type and request.user.type.type_of_user == 1:
        restaurant = request.user.type.restaurant
        rest_views.restaurant = restaurant
        return redirect('restaurants/cashier')
    elif request.user.is_authenticated and request.user.type and request.user.type.type_of_user == 2:
        restaurant = request.user.type.restaurant
        rest_views.restaurant = restaurant
        return redirect('restaurants/restaurant_admin')
    table_code = request.GET.get('table_code')
    if table_code:
        table = restaurants.search_table(table_code)
        if table:
            restaurant = table.restaurant
            products = restaurant.product_set.all()
            rest_views.table = table
            rest_views.restaurant = restaurant
            rest_views.products = products
            return redirect('restaurants/menu')
    return render(request, 'home.html', {'table_code': table_code})
