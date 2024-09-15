from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(verbose_name='image', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'

