from rest_framework.permissions import IsAdminUser
from product.models import Product
from rest_framework import generics
from product.serializers import ProductSerializers
from product.pagination import MyPagination

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializers
    pagination_class = MyPagination

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializers