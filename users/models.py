from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    MODERATOR = 'moderator'
    MEMBER = 'member'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='телефон')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='город')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='аватарка')
    role = models.CharField(max_length=30, verbose_name='role', choices=UserRole.choices, default='member')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'