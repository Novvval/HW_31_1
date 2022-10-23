from datetime import datetime, date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from ads.validators import check_if_true, check_age, check_email


class Category(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Админ"
        MEMBER = "member", "Пользователь"
        MODERATOR = "moderator", "Модератор"

    birth_date = models.DateField(null=True, validators=[check_age])
    email = models.EmailField(unique=True, default="email@test.com", validators=[check_email])
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=9, choices=Role.choices, default=Role.MEMBER)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    location_id = models.ManyToManyField(Location, null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Ad(models.Model):
    name = models.CharField(max_length=1000, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False, validators=[check_if_true])
    image = models.ImageField(upload_to="ads/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
