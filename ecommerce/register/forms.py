from django import forms
from django.utils.translation import ugettext_lazy as translate
from .models import validate_cep, validate_cnpj, validate_phone_number, GENDER_CHOICES


class RegisterForm(forms.Form):
    name = forms.CharField(label=translate("Nome"))
    last_name = forms.CharField(label=translate("Sobrenome"))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial="M", widget=forms.Select(), required=True)
    login = forms.CharField(label=translate("Usuário"))
    email = forms.CharField(label="E-mail")
    phone_number = forms.CharField(label=translate("Celular"), validators=[validate_phone_number])
    address = forms.CharField(label=translate("Endereço"))
    postal_code = forms.CharField(label=translate("CEP"), validators=[validate_cep])
    cpf = forms.CharField(label="CPF", validators=[validate_cnpj])
    city = forms.CharField(label=translate("Cidade"))
    state = forms.CharField(label=translate("Estado"))
