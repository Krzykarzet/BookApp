from django.contrib import admin
from .models import Publisher, Book, Author, LiteraryGenre

# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(LiteraryGenre)
admin.site.register(Book)
