from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class LiteraryGenre(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    genre = models.ManyToManyField(LiteraryGenre)
    page_count = models.IntegerField(default=None, blank=True, null=True)
    published_year = models.IntegerField(default=None, blank=True, null=True)
    ISBN_10 = models.CharField(max_length=10)
    ISBN_13 = models.CharField(max_length=13)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.title


