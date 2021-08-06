from django.db import connection
from contextlib import closing
from collections import OrderedDict
from rest_framework.exceptions import NotFound

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_category_all():
    categories = query_get_category_all()
    items = []
    for data in categories:
        items.append(
            OrderedDict(
                {
                    "id": data['id'],
                    "first_name": data['first_name'],
                    "last_name": data['last_name'],
                    "age": data['age']
                }
            )
        )
    return items


def get_category_one(category_id):
    category = query_get_category_one(category_id)
    return OrderedDict(
        {
            "id": category['id'],
            "title": category['title'],
            "created_at": category['created_at']
        }
    )


def query_get_category_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """SELECT * FROM myapi_category""")
        categories = dictfetchall(cursor)
    return categories


def query_get_category_one(category_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM myapi_category WHERE id = %s""", [category_id])
        category = dictfetchone(cursor)
    return category

############################################################################################


def get_product_all():
    products = query_get_product_all()
    items = []
    for data in products:
        items.append(
            OrderedDict(
                {
                    "id": data['id'],
                    "title": data['title'],
                    "description": data['description'],
                    "cost": data['cost'],
                    "price": data['price'],
                }
            )
        )
    return items


def get_product_one(product_id):
    product = query_get_product_one(product_id)
    return OrderedDict(
        {
            "id": product['id'],
            "title": product['title'],
            "created_at": product['created_at']
        }
    )


def query_get_product_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """SELECT * FROM myapi_product""")
        products = dictfetchall(cursor)
    return products


def query_get_product_one(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM myapi_product WHERE id = %s""", [product_id])
        product = dictfetchone(cursor)
    return product
