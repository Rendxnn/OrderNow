from .models import Table


def search_table(table_code):
    try:
        table = Table.objects.get(code=table_code)
    except:
        table = None
    return table
