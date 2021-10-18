from django.forms import ModelForm, fields, models

from .models import Client


class AddClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
