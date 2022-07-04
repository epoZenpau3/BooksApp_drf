from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookApiView)


urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookApiView.as_view()),
    path('book/create/', views.BookApiCreateView.as_view()),
    path('book/detail/<int:pk>/', views.BookApiDetailView.as_view()),
    path('author/', views.AuthorApiView.as_view()),
    path('author/detail/<int:pk>/', views.AuthorApiDetailView.as_view()),
]
