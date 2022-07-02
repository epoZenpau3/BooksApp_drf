from rest_framework import serializers
from .models import Books, Author


class BookSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.name')
    author_second_name = serializers.CharField(source='author.second_name')

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'color', 'author_first_name', 'author_second_name']


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'color']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
