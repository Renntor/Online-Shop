from rest_framework import serializers
from category.serializers import CategoryCartSerializers
from subcategory.models import Subcategory


class SubcategorySerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        slug = validated_data('slug')
        subcategory = Subcategory(**validated_data)
        subcategory.slug(slug)
        subcategory.save()
        return subcategory

    class Meta:
        model = Subcategory
        fields = ('name', 'image',)
        lookup_field = 'slug'
        extra_kwargs = {'slug': {'read_only': True}}


class SubcategoryCartSerializers(serializers.ModelSerializer):
    category = CategoryCartSerializers()

    class Meta:
        model = Subcategory
        fields = ('name', 'category',)
