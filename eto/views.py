from django.db import models
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from bl.models import BL
from lc.models import LC
from .forms import AddTerminalForm, AddPQAForm


    
class AddTerminalView(ListView):
    model = BL
    template_name = 'eto/bl_list.html'
    context_object_name = 'bls'

class AddPayorderView(ListView):
    model = LC
    template_name = 'eto/wharfage_list.html'
    context_object_name = 'lcs'

class UpdatePQAView(UpdateView):
    model = LC
    template_name = 'eto/add_wharfage.html'
    form_class = AddPQAForm
    success_url = reverse_lazy('wharfage_list')
    
    
class BLListView(ListView):
    model = LC
    template_name = 'eto/allow_list.html'
    context_object_name = 'lcs'

    
class UpdateTerminalView(UpdateView):
    model = BL
    template_name = 'eto/add_terminal.html'
    form_class = AddTerminalForm
    success_url = reverse_lazy('bl_list')

class BondListView(ListView):
    model = BL
    template_name = 'eto/ibond.html'
    context_object_name = 'bls'
    

