from rest_framework import serializers
from product.models import Product, Cart, ProductImage
from subcategory.serializers import SubcategoryCartSerializers


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializers(serializers.ModelSerializer):
    subcategory = SubcategoryCartSerializers()
    image = ProductImageSerializers(many=True, read_only=True)

    def create(self, validated_data):
        slug = validated_data('slug')
        category = Product(**validated_data)
        category.slug(slug)
        category.save()
        return category

    class Meta:
        model = Product
        fields = ('name', 'price', 'subcategory', 'image',)
        lookup_field = 'slug'
        extra_kwargs = {'slug': {'read_only': True}}


class CartCreateUpdateSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    def validate(self, data):
        if (data.get("product", None) is None ) or (data.get('quantity', None) is None):
            raise serializers.ValidationError(
                'You must enter the product name and quantity'
            )

        return data

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
