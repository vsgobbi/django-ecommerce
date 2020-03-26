from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as translate
from django.db import models
from re import match


def validate_cnpj(cpf):
    cpf_expression = r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}"
    if not match(cpf_expression, cpf):
        raise ValidationError("CPF inválido!", params={'cpf': cpf},)


def validate_cep(cep):
    cep_expression = r"^[0-9]{5}-[0-9]{3}$"
    if not match(cep_expression, cep):
        raise ValidationError("CEP inválido, exemplo: 04159-040")


def validate_phone_number(phone_number):
    phone_number_expression = r"^[0-9]{11}$"
    if not match(phone_number_expression, phone_number):
        raise ValidationError("Celular inválido, insira como exemplo: 18997133400")


GENDER_CHOICES = (
    ("M", translate("Masculino")),
    ("F", translate("Feminino")),
    ("N", translate("Não declarar")),
)


class Users(models.Model):
    login = models.CharField(blank=False, unique=True, null=False, max_length=30)
    name = models.CharField(max_length=99, null=False)
    last_name = models.CharField(max_length=99, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, default="M", max_length=1)
    phone_number = models.CharField(max_length=99, null=False, validators=[validate_phone_number])
    email = models.CharField(max_length=99, null=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    address = models.CharField(max_length=150, null=False)
    postal_code = models.CharField(max_length=30, null=False)
    cpf = models.CharField(max_length=30, null=False, db_index=True, validators=[validate_cnpj])
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)

    USERNAME_FIELDS = "login"
    REQUIRED_FIELDS = ["login", "name", "last_name", "email", "phone_number"]

    def __str__(self):
        return self.text
