from rest_framework.permissions import IsAdminUser
from category.models import Category
from rest_framework import generics
from category.serializers import CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializers

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializers

