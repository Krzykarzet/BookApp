from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Publisher, LiteraryGenre, Author, Country
from .forms import BookForm
import requests


# Create your views here.
def index(request):
    # return HttpResponse('helo helo index')
    return render(request, 'index.html')


def booklist(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', {'books': books})


def newbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
    else:
        form = BookForm()
    return render(request, 'newbook.html', {'form': form})
    # return render(request, 'newbook.html')


def importbook(request):
    return render(request, 'importbooks.html')


def api_request(request):
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=lord+of+the+rings')
    data = response.json()
    return render(request, 'api_data.html', {'items': data['items']})
