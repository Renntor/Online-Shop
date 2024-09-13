from product.models import Product
from rest_framework import generics
from product.serializers import ProductSerializers
from product.pagination import MyPagination

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = MyPagination

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
