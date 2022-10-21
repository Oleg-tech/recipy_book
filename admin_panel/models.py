from django.db import models


class Users(models.Model):
    id = models.IntegerField(verbose_name="ID").primary_key
    first_name = models.CharField(max_length=50, null=True, default=None, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, null=True, default=None, verbose_name="Прізвище")
    username = models.CharField(max_length=30, null=True, default=None, verbose_name="Ім'я користувача")
    register_name = models.CharField(max_length=255, null=True, default=None, verbose_name="Ім'я з анкети")
    sex = models.CharField(max_length=20, default="", verbose_name="Стать")

    class Meta:
        verbose_name_plural = "Користувачі"
        ordering = ['username']


class Recipes(models.Model):
    name = models.CharField(max_length=50, null=True, default=None, verbose_name="Назва")
    discription = models.CharField(max_length=400, null=True, default=None, verbose_name="Опис")
    image = models.CharField(max_length=100, null=True, default=None, verbose_name="Фото")

    class Meta:
        verbose_name_plural = "Рецепти"
        ordering = ['name']
