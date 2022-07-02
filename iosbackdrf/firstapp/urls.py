from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookApiView)


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookApiView.as_view()),
    path('books/create/', views.BookApiCreateView.as_view()),
    path('books/detail/<int:pk>/', views.BookApiDetailView.as_view()),
    path('authors/', views.AuthorApiView.as_view()),
    path('authors/create/', views.AuthorApiCreateView.as_view()),
    path('authors/detail/<int:pk>/', views.AuthorApiDetailView.as_view()),
]
