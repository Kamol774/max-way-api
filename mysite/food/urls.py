from django.urls import path
from .views import CategoryProductView

urlpatterns = [
    path('category-products/', CategoryProductView.as_view(), name='category-products')
]