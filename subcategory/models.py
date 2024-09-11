from django.db import models
from category.models import Category

class Subcategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural ='subcategories'
