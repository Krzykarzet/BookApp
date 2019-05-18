from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Publisher, LiteraryGenre, Author, Country


# Create your views here.
def index(request):
    # return HttpResponse('helo helo index')
    return render(request, 'index.html')


def booklist(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', {'books': books})


def newbook(request):
    return render(request, 'newbook.html')


def importbook(request):
    return render(request, 'importbooks.html')
