from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', null=True, blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
