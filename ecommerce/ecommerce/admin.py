from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Product, ProductAdmin)
