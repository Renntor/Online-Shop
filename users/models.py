from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural =' users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []