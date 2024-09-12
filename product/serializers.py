from rest_framework import serializers
from product.models import Product

class ProductSerializers(serializers.ModelSerializer):


    def create(self, validated_data):
        slug = validated_data('slug')
        category = Product(**validated_data)
        category.slug(slug)
        category.save()
        return category


    class Meta:
        model = Product
        field = ('name', 'price', )
        extra_kwargs = {'slug': {'read_only': True}}