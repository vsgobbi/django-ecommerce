from django.contrib import admin
from ecommerce.shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "last_price", "price", "stock", "available", "created_at", "updated_at"]
    list_filter = ["available", "created_at", "updated_at"]
    list_editable = ["price", "stock", "available"]
    prepopulated_fields = {"slug": ("nome",)}


admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Agig Ltda E-COMMERCE"
