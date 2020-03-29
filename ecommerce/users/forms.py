from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from django.utils.translation import ugettext_lazy as translate
from .models import validate_cep, validate_cpf, validate_phone_number, GENDER_CHOICES, Users, Address


class SignIn(UserCreationForm):
    login = forms.CharField(max_length=30, required=True, help_text='Campo necessário!', label='Login')

    class Meta:
        model = Users
        fields = ('login', 'password')


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ["name", "last_name", "gender", "login", "password", "email", "phone_number", "cpf", "birthdate"]
        field_order = ["login", "password", "name", "last_name", "email", "phone_number", "cpf", "birthdate"]

    name = forms.CharField(label=translate("Nome"))
    last_name = forms.CharField(label=translate("Sobrenome"))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label=translate("Gênero"),
        initial="M",
        widget=forms.Select(),
        required=True
    )
    login = forms.CharField(label=translate("Usuário"))
    password = forms.CharField(max_length=20, required=True, label=translate("Senha"), widget=forms.PasswordInput)
    email = forms.CharField(label="E-mail")
    phone_number = forms.CharField(label=translate("Celular"), validators=[validate_phone_number])
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
    birthdate = forms.DateField(
        label=translate("Nascimento"),
        input_formats="%d/%m/%Y",
        error_messages={"invalid": "Insira data de nascimento formatada, ex: 01/01/2002"},
        widget=DateInput(
            attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'

            })
    )


class AddressRegisterForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["addressLine1", "addressLine2", "postal_code", "city", "state", "cpf"]

    addressLine1 = forms.CharField(label=translate("Endereço"))
    addressLine2 = forms.CharField(label=translate("Complemento"))
    postal_code = forms.CharField(label=translate("CEP"), validators=[validate_cep])
    name = forms.CharField(label=translate("Nome"))
    city = forms.CharField(label=translate("Cidade"))
    state = forms.CharField(label=translate("Estado"))
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
