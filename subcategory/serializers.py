from rest_framework import serializers
from subcategory.models import Subcategory

class SubcategorySerializers(serializers.ModelSerializer):


    def create(self, validated_data):
        slug = validated_data('slug')
        category = Subcategory(**validated_data)
        category.slug(slug)
        category.save()
        return category


    class Meta:
        model = Subcategory
        field = ('name', 'image', )
        extra_kwargs = {'slug': {'read_only': True}}