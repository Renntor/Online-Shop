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
        fields = ('name', 'image',)
        lookup_field = 'slug'
        extra_kwargs = {'slug': {'read_only': True}}


class CategoryCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
