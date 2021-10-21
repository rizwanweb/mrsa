from django.db import models
from django.shortcuts import render

from django.views.generic.list import ListView

from bl.models import BL
from lc.models import LC

# Create your views here.

#class AddTerminalView(ListView):
    # models = BL
    # template_name = 'eto/bl_list.html'
    # context_object_name = 'bls'

    
class AddTerminalView(ListView):
    model = BL
    template_name = 'eto/bl_list.html'
    context_object_name = 'bls'

