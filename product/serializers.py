from rest_framework import serializers
from product.models import Product, Cart


class ProductSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        slug = validated_data('slug')
        category = Product(**validated_data)
        category.slug(slug)
        category.save()
        return category

    class Meta:
        model = Product
        fields = ('name', 'price', 'subcategory',)
        extra_kwargs = {'slug': {'read_only': True}}


class CartCreateUpdateSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Cart
        fields = ('product', 'product_name', 'quantity')


class CartDestroy(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('product',)

class CartsDestroy(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = '__all__'