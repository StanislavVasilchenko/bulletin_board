from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    # TODO закончите enum-класс для пользователя
    ADMIN = 'admin', _('Admin')
    USER = 'user', _('User')


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    objects = UserManager()

    username = None

    first_name = models.CharField(max_length=150, verbose_name='first name', blank=True)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=20, verbose_name='phone number')
    role = models.CharField(choices=UserRoles.choices, max_length=20, verbose_name='role', default=UserRoles.USER)
    image = models.ImageField(upload_to='users/image/', verbose_name='image', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
