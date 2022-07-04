from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookViewSet.as_view({'get': 'list'})),
    path('book/detail/<int:pk>/', views.BookViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
    path('book/create/', views.AuthorViewSet.as_view({'post': 'create'})),
    path('author/', views.AuthorViewSet.as_view({'get': 'list'})),
    path('author/detail/<int:pk>/', views.AuthorViewSet.as_view({'post': 'create'})),
]
