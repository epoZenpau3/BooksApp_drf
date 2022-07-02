from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions
from .serializers import BookSerializer
from . models import Books


def index(request):
    return HttpResponse("Я тут был и создал, но не добавил.")


class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
