from django import forms
from django.utils.translation import ugettext_lazy as translate
from shop.models import Product


class SearchProductForm(forms.Form):

    class Meta:
        model = Product
        fields = "name"

    name = forms.CharField(label=translate("Nome"), max_length=100)
    description = forms.CharField(label=translate("Descrição"), max_length=100)

