from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='name')
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'

