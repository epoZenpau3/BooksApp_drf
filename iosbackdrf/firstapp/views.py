from django.http import HttpResponse
from rest_framework import generics
from .serializers import BookSerializer, BookCreateSerializer
from .models import Books, Author


def index(request):
    return HttpResponse("Я тут был и создал, но не добавил.")


class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookApiCreateView(generics.CreateAPIView):
    serializer_class = BookCreateSerializer


class AuthorApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = BookCreateSerializer


class AuthorApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = BookCreateSerializer
