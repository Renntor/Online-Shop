from subcategory.models import Subcategory
from rest_framework import generics
from subcategory.serializers import SubcategorySerializers
from subcategory.pagination import MyPagination


class SubcategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
    pagination_class = MyPagination
    lookup_field = 'slug'


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
