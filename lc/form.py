from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.widgets import DateInput

from .models import LC


class AddLCForm(ModelForm):
    class Meta:
        model = LC
        fields = '__all__'

        # widgets = {
        #     'igmDate': DateInput(attr)
        # }
