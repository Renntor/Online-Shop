from category.models import Category
from rest_framework import generics
from category.serializers import CategorySerializers
from category.pagination import MyPagination


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = MyPagination
    lookup_field = 'slug'


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
