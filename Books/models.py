from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)


class LiteraryGenre:
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genre = models.ManyToManyField(LiteraryGenre)
    page_count = models.IntegerField
    published_year = models.IntegerField
    ISBN_10 = models.CharField(max_length=10)
    ISBN_13 = models.CharField(max_length=13)


