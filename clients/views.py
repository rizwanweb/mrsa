from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from clients.models import Client
from clients.forms import AddClientForm


class AddClientView(CreateView):
    model = Client
    form_class = AddClientForm
    template_name = 'clients/add_client.html'
    context_object_name = 'client'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UpdateClientView(UpdateView):  # Update Client View
    model = Client
    template_name = 'clients/add_client.html'
    form_class = AddClientForm
    context_object_name = 'client'
    success_url = reverse_lazy('client_list')


class ListClientView(ListView):  # List Client View
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'


class DetailClientView(DetailView):  # List Client View
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'
