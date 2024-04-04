from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("user", "User")
    ]
    username = None

    first_name = models.CharField(max_length=150, verbose_name='first name', blank=True)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=20, verbose_name='phone number')
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, verbose_name='role', default='user')
    image = models.ImageField(upload_to='users/image/', verbose_name='image', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
