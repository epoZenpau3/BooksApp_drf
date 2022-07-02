from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.name')
    author_second_name = serializers.CharField(source='author.second_name')

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'color', 'author_first_name', 'author_second_name']

