from unicodedata import category
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'slug', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_field = {'slug': ('name',)}
