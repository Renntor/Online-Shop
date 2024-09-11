from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='name')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'

