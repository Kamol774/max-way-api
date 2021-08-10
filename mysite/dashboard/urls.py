from django.urls import path
from .views import CategoryView, ProductView, CustomerView, OrderView, OrderProductView
urlpatterns = [
    path('category/list/', CategoryView.as_view(), name='category-list'),
    path('category/<int:pk>/retrieve', CategoryView.as_view(), name='category-retrieve'),
    path('category/create/', CategoryView.as_view(), name='category-create'),
    path('category/<int:pk>/destroy', CategoryView.as_view(), name='category-destroy'),  # bitta objectni delete qilish uchun
    path('category/<int:pk>/update', CategoryView.as_view(), name='category-update'),

    path('product/list/', ProductView.as_view(), name='product-list'),
    path('product/<int:pk>/retrieve', ProductView.as_view(), name='product-retrieve'),
    path('product/create/', ProductView.as_view(), name='product-create'),
    path('product/<int:pk>/destroy', ProductView.as_view(), name='product-destroy'),    # bitta objectni delete qilish uchun
    path('product/<int:pk>/update', ProductView.as_view(), name='product-update'),

    path('order/list/', OrderView.as_view(), name='order-list'),
    path('order/<int:pk>/update', OrderView.as_view(), name='order-update'),

    path('customer/list/', CustomerView.as_view(), name='customer-list'),

    path('orderproduct/list/', OrderProductView.as_view(), name='orderproduct-list'),
]