from django.shortcuts import render

# Views Import
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'base/index.html'


