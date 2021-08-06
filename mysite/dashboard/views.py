from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from food.models import Category, Product, Customer, Order, OrderProduct
from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderProductSerializer

# Create your views here.

class CategoryView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            model = Category.objects.get(pk=pk)
        except Exception:
            raise NotFound("Category not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            category = self.get_object(kwargs.get("pk"))
            serializer = CategorySerializer(category, many=False)
            return Response(serializer.data)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        serializer = CategorySerializer(data=request.data, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        category = self.get_object(kwargs.get("pk"))
        category.delete()
        return Response({"state": "deleted"})

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
            product = self.get_object(kwargs.get("pk"))
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        product = self.get_object(kwargs.get("pk"))
        serializer = ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        product = self.get_object(kwargs.get("pk"))
        product.delete()
        return Response({"state": "deleted"})

class CustomerView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            model = Customer.objects.get(pk=pk)
        except Exception:
            raise NotFound("Customer not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            customer = self.get_object(kwargs.get("pk"))
            serializer = CustomerSerializer(customer, many=False)
            return Response(serializer.data)
        else:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)

class OrderView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            model = Order.objects.get(pk=pk)
        except Exception:
            raise NotFound("Order not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            order = self.get_object(kwargs.get("pk"))
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        order = self.get_object(kwargs.get("pk"))
        serializer = OrderSerializer(data=request.data, instance=order)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderProductView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            model = OrderProduct.objects.get(pk=pk)
        except Exception:
            raise NotFound("OrderProduct not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            orderProduct = self.get_object(kwargs.get("pk"))
            serializer = OrderProductSerializer(orderProduct, many=False)
            return Response(serializer.data)
        else:
            orderProducts = Customer.objects.all()
            serializer = OrderProductSerializer(orderProducts, many=True)
            return Response(serializer.data)
