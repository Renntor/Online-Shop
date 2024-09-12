from django.db import models
from subcategory.models import Subcategory

class Product(models.Model):

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='subcategory')
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(null=True, blank=True, unique=True)
    price = models.PositiveIntegerField(verbose_name='price')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural ='products'

class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    image = models.ImageField(verbose_name='image')
