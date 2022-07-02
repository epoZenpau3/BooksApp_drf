from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookApiView)


urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', views.BookApiView.as_view()),
]
