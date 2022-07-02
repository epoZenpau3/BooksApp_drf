from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='index'),
    path('firstapp/', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]