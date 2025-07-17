from django.db import models
from django.utils.text import slugify

class Dishes_Category(models.Model):
    type = models.CharField(max_length=100, verbose_name='Категория блюда', unique=True)

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'
        ordering = ['id']

    def __str__(self):
        return self.type


class Dishes(models.Model):
    dishes_name = models.CharField(max_length = 150, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    photo = models.ImageField(verbose_name = 'Фотография', upload_to = 'dishes/')
    category = models.ForeignKey('Dishes_Category', on_delete = models.PROTECT, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    contact = models.CharField(max_length=50, verbose_name='Номер телефона')

    def __str__(self):
        return f"{self.name} — {self.contact}"

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

