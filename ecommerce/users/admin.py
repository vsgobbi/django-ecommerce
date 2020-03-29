import logging
from django.contrib import admin
from .forms import UserRegisterForm
from .models import Users

logger = logging.getLogger(__name__)


class CustomUserAdmin(admin.ModelAdmin):
    add_form = UserRegisterForm
    model = Users
    list_display = ["email", "login", "name", "cpf"]
    list_filter = ["created_at", ]


try:
    admin.site.register(Users, CustomUserAdmin)
    admin.site.site_header = "Agig Ltda E-COMMERCE"
except Exception as e:
    logger.exception("Não foi possível criar usuário %s", e)
