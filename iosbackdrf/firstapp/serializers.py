from rest_framework import serializers
from .models import Books, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'color']


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'color']


class BookCreateSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'second_name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books')
        author, created = Author.objects.update_or_create(**validated_data)
        for books_data in books_data:
            Books.objects.create(author=author, **books_data)
        return author
