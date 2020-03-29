import logging
from django.contrib import admin
from shop.models import Category, Product

logger = logging.getLogger(__name__)


class CategoryAdmin(admin.ModelAdmin):
    Category.name = "Promoção"
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# try:
#     admin.site.register(CategoryAdmin, CategoryAdmin)
#     logger.info("Nova categoria 'Promoção' criada %s", Category)
# except:
#     logger.exception("Não foi possível criar categoria")


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'last_price', 'price', 'available', 'created_at', 'updated_at']
    # list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['last_price', 'price', 'available']
    # prepopulated_fields = {'slug': ('name',)}


# try:
#     admin.site.register(Product, ProductAdmin)
#     logger.info("Nova promoção criada %s", Product)
# except:
#     logger.exception("Não foi possível criar promoção")
