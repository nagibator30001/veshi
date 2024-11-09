# Generated by Django 5.1.3 on 2024-11-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('logo', models.ImageField(upload_to='media/', verbose_name='Логотип')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
