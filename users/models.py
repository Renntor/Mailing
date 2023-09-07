from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    mail_key = models.CharField(max_length=30, default='', verbose_name='key')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
