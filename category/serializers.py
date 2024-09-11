from rest_framework import serializers
from category.models import Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('name')
        extra_kwargs = {'slug': {'read_only': True}}