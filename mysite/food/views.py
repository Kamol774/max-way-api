from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView

from food import services
from food.models import Category, Product, Customer, Order, OrderProduct
from dashboard.serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderProductSerializer

# Create your views here.

class CategoryProductView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        category_products = services.get_category_products()
        return Response(category_products)


class ProductView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            model = Product.objects.get(pk=pk)
        except Exception:
            raise NotFound("Product not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            product = services.get_product_one(kwargs.get("pk"))
            return Response(product)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)


class CustomerView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #
    # def get_object(self, pk):
    #     try:
    #         model = Customer.objects.get(pk=pk)
    #     except Exception:
    #         raise NotFound("Customer not found -----------")
    #     return model
    #
    # def get(self, request, *args, **kwargs):
    #     if kwargs.get("pk"):
    #         customer = self.get_object(kwargs.get("pk"))
    #         serializer = CustomerSerializer(customer, many=False)
    #         return Response(serializer.data)
    #     else:
    #         customers = Customer.objects.all()
    #         serializer = CustomerSerializer(customers, many=True)
    #         return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrderView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_object(self, pk):
    #     try:
    #         model = Order.objects.get(pk=pk)
    #     except Exception:
    #         raise NotFound("Order not found -----------")
    #     return model
    #
    # def get(self, request, *args, **kwargs):
    #     if kwargs.get("pk"):
    #         order = self.get_object(kwargs.get("pk"))
    #         serializer = OrderSerializer(order, many=False)
    #         return Response(serializer.data)
    #     else:
    #         orders = Order.objects.all()
    #         serializer = OrderSerializer(orders, many=True)
    #         return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderProductView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = OrderProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



def get(self, request, *args, **kwargs):
    if kwargs.get("pk"):
        book = services.get_book_one(kwargs.get("pk"))
        return Response(book)
    else:
        books = services.get_book_all()
        return Response(books)