from rest_framework.permissions import IsAdminUser
from subcategory.models import Subcategory
from rest_framework import generics
from subcategory.serializers import SubcategorySerializers
from subcategory.pagination import MyPagination

class SubcategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SubcategorySerializers
    pagination_class = MyPagination

class SubcategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SubcategorySerializers