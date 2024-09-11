from unicodedata import category

from rest_framework import serializers
from category.models import Category

class CategorySerializers(serializers.ModelSerializer):


    def create(self, validated_data):
        slug = validated_data('slug')
        category = Category(**validated_data)
        category.slug(slug)
        category.save()
        return category


    class Meta:
        model = Category
        field = ('name', 'image', )
        extra_kwargs = {'slug': {'read_only': True}}