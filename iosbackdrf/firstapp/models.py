from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)

    # class Meta:
    #     unique_together = ('name', 'second_name')


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
