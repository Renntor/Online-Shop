from django.contrib import admin
from subcategory.models import Subcategory


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image' )
    prepopulated_fields = {'slug': ('name',)}