from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'index.html'
