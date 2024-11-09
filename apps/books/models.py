from django.db import models

# Create your models here.
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
        