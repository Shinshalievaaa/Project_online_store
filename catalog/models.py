from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание')
    image_product = models.ImageField(upload_to='photo/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='products', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']
