from django.contrib import admin
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='index'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('firstapp/', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]