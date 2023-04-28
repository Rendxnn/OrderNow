from django.shortcuts import render


def home(request):
    table_code = request.GET.get('table_code')
    return render(request, 'home.html', {'table_code': table_code})

# hola
