from django.db import connection
from contextlib import closing
from collections import OrderedDict
from rest_framework.exceptions import NotFound
import json

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


def get_category_products():
    category_products = query_category_products()
    items = []
    for category_product in category_products:
        items.append(
            OrderedDict(
                {
                    "id": category_product["id"],
                    "title": category_product["title"],
                    "product": json.loads(category_product["title"]),
                }
            )
        )
    return items


def query_category_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """with table1 as (SELECT c.*, (SELECT JSONB_AGG(v) FROM (SELECT food_product.* FROM food_product WHERE 
            food_product.category_id = c.id) v) AS products FROM food_category c)
            select table1.* from table1 where table1.products is not null;"""
        )
        category_products = dictfetchall(cursor)
    return category_products



#############################################################################################

# def get_book_all():
#     books = query_get_book_all()
#     items = []
#     for data in books:
#         items.append(
#             OrderedDict(
#                 {
#                     "id": data['id'],
#                     "name": data['name'],
#                     "category": {
#                         "id": data['category_id'],
#                         "name": data['category_name']
#                     },
#                     "author": {
#                         "id": data['author_id'],
#                         "first_name": data['first_name']
#                     },
#                     "description": data['description'],
#                 }
#             )
#         )
#     return items
#
#
# def get_book_one(book_id):
#     book = query_get_author_one(book_id)
#     return OrderedDict(
#             {
#                 "id": book['id'],
#                 "name": book['name'],
#                 "category": {
#                     "id": book['category_id'],
#                     "name": book['category_name']
#                 },
#                 "author": {
#                     "id": book['author_id'],
#                     "first_name": book['first_name']
#                 },
#                 "description": book['description'],
#             }
#         )
#
#
# def query_get_book_all():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute(
#             """SELECT myapi_book.*, myapi_author.first_name, myapi_category.name as category_name FROM myapi_book
#             INNER JOIN myapi_author ON myapi_book.author_id = myapi_author.id
#             INNER JOIN myapi_category ON myapi_book.category_id = myapi_category.id""")
#         books = dictfetchall(cursor)
#     return books
#
#
# def query_get_book_one(book_id):
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""SELECT myapi_book.*, myapi_author.first_name, myapi_category.name as category_name FROM myapi_book
#             INNER JOIN myapi_author ON myapi_book.author_id = myapi_author.id
#             INNER JOIN myapi_category ON myapi_book.category_id = myapi_category.id
#             WHERE myapi_book.id = %s""", [book_id])
#         book = dictfetchone(cursor)
#     return book