from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        
class Book(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название книги'
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор'
    )
    publication_date = models.DateField(
        verbose_name='Дата публикации'
    )
    logo = models.ImageField(
        upload_to='media/',
        verbose_name='Логотип'
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name='В наличии'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        