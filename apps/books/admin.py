from django.contrib import admin
from apps.books.models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):	
	list_display = ['id', 'title', 'author', 'publication_date', 'logo', 'in_stock']
	