from django.contrib.auth.models import AbstractUser
from django.db import models
from users.services import random_key


# Create your models here.


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    mail_key = models.CharField(max_length=30, default=random_key(), verbose_name='ключ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
