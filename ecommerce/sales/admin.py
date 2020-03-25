import logging
from django.contrib import admin
from .models import Category, Product

logger = logging.getLogger(__name__)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


try:
    admin.site.register(Category, CategoryAdmin)
    logger.info("Nova categoria criada %s", Category)
except:
    logger.exception("Nao foi possivel criar categoria")


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'last_price', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


try:
    admin.site.register(Product, ProductAdmin)
    logger.info("Nova promocao criada %s", Product)
except:
    logger.exception("Nao foi possivel criar promocao")
