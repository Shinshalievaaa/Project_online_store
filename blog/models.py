from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержимое')
    image_blog = models.ImageField(upload_to='photo/', null=True, blank=True, verbose_name='Превью (изображение)')
    count_views = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    is_publication = models.BooleanField(verbose_name='Признак публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['name']
