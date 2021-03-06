from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'authors', 'description', 'genre', 'page_count', 'published_year', 'publisher', 'ISBN_10',
                  'ISBN_13')
