from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class UserRole(models.TextChoices):
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    role = models.CharField(max_length=15, verbose_name='роль', choices=UserRole.choices, default=UserRole.MEMBER)

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'
