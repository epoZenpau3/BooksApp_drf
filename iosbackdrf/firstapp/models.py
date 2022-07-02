from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
