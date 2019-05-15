from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('helo helo index')
    return render(request, 'index.html')


def booklist(request):
    return render(request, 'booklist.html')


def newbook(request):
    return render(request, 'newbook.html')


def importbook(request):
    return render(request, 'importbooks.html')
