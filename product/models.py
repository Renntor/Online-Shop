from django.db import models
from django.db.models import CASCADE


from subcategory.models import Subcategory
from users.models import User


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='subcategory')
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(null=True, blank=True, unique=True)
    price = models.PositiveIntegerField(verbose_name='price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image', verbose_name='product')
    image = models.ImageField(verbose_name='image')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    quantity = models.PositiveIntegerField(default=1, verbose_name='quantity')

    def price_calculation(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
