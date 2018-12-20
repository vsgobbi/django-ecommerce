#from django.db import models
# Create your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth import get_user_model
#User = get_user_model()


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

'''
class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
'''
