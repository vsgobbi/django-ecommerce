from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as translate

RATING = [
    ("S", translate("Super")),
    ("M", translate("Muito")),
    ("P", translate("Pouco")),
    ("N", translate("Nenhuma")),
]


class Category(models.Model):
    name = models.CharField(translate("Nome"), max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name", )
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(translate("Nome"), max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    cart_added = models.PositiveIntegerField(editable=False, null=True)
    description = models.TextField(translate("Descrição"), blank=True)
    last_price = models.DecimalField(translate("Valor anterior"), max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(translate("Valor atual"), max_digits=10, decimal_places=2,  null=False)
    available = models.BooleanField(translate("Disponível"), default=True)
    stock = models.PositiveIntegerField(translate("Quantidade em estoque"), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(translate("Imagem"), upload_to="products/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ("name", "available", "price")
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:75]

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
