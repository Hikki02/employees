from apps.department.models import Department

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.db import models

from apps.user.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=100, verbose_name='')
    last_name = models.CharField(max_length=100, verbose_name='')
    position = models.CharField(max_length=100, verbose_name='')
    hire_date = models.DateField(null=True, blank=True, verbose_name='Дата према на работу')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    username = models.CharField(max_length=225, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_active = models.BooleanField(default=False, verbose_name='Активен')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ()

    objects = UserManager()

    def __str__(self):
        return f'{self.id} -- {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
