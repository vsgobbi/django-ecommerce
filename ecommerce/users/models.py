import logging
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as translate
from django.db import models
from datetime import datetime, timedelta
from re import match

logger = logging.getLogger(__name__)


def validate_cpf(cpf):
    cpf_expression = r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}"
    if not match(cpf_expression, cpf):
        raise ValidationError(translate("CPF inválido!"), params={'cpf': cpf},)


def validate_cep(cep):
    cep_expression = r"^[0-9]{5}-[0-9]{3}$"
    if not match(cep_expression, cep):
        raise ValidationError(translate("CEP inválido, exemplo: 04159-040"))


def validate_phone_number(phone_number):
    phone_number_expression = r"^[0-9]{11}$"
    if not match(phone_number_expression, phone_number):
        raise ValidationError(translate("Celular inválido, insira como exemplo: 18997133400"))


def validate_birthdate(birthdate):
    today = datetime.today()
    minimumAccept = (today - timedelta(days=365*18)).date()
    try:
        if birthdate > minimumAccept:
            raise ValidationError(translate("Usuário deve ser maior de idade!"))
    except Exception as error:
        logger.warning("Erro ao validar data de nascimento, {}".format(error))
        raise ValidationError(translate("Data de nascimento inválida!"))


GENDER_CHOICES = (
    ("M", translate("Masculino")),
    ("F", translate("Feminino")),
    ("N", translate("Não declarar")),
)

ADDRESS_TYPES = (
    ("1", translate("Residencial")),
    ("2", translate("Comercial")),
    ("N", translate("Não declarar")),
)


class Address(models.Model):

    name = models.CharField("Nome completo", max_length=99, null=False)
    addressLine1 = models.CharField("Endereço", max_length=256, null=False)
    addressLine2 = models.CharField("Complemento", max_length=128)
    postal_code = models.CharField("CEP", max_length=30, null=False)
    city = models.CharField(translate("Cidade"), max_length=100, null=False)
    state = models.CharField(translate("Estado"), max_length=100, null=False)
    cpf = models.CharField(max_length=30, null=False, db_index=True, validators=[validate_cpf])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('city', "state")

    def __str__(self):
        return self.addressLine1


class Users(models.Model):
    login = models.CharField(blank=False, unique=True, null=False, max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=99, null=False)
    last_name = models.CharField(max_length=99, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, default="M", max_length=1)
    birthdate = models.DateField(default="01/01/1990", null=False, validators=[validate_birthdate])
    phone_number = models.CharField(max_length=99, null=False, validators=[validate_phone_number])
    email = models.CharField(max_length=99, null=False, db_index=True)
    cpf = models.CharField(max_length=30, null=False, db_index=True, validators=[validate_cpf])
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE)

    USERNAME_FIELDS = "login"
    REQUIRED_FIELDS = ["login", "name", "last_name", "email", "phone_number"]

    class Meta:
        ordering = ('name', )

    def get_full_name(self):
        full_name = '%s %s' % (self.name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.login, self.name, self.last_name, self.email)

