from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from lc.form import AddLCForm

from lc.models import LC

# Create your views here.


class AddLCView(CreateView):
    model = LC
    template_name = 'lc/create_lc.html'
    form_class = AddLCForm
    success_url = reverse_lazy('add_bl')


class UpdateLCView(UpdateView):
    model = LC
    template_name = 'lc/create_lc.html'
    form_class = AddLCForm
    success_url = reverse_lazy('lc_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        bls = instance.bl_set.all()
        for bl in bls:
            bl.save()

        return super().form_valid(form)


class ListLCView(ListView):
    model = LC
    template_name = 'lc/lc_list.html'
    context_object_name = 'lcs'
