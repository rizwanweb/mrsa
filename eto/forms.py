from django.forms import ModelForm, fields


from bl.models import BL


class AddTerminalForm(ModelForm):
    class Meta:
        model = BL
        fields = ['terminal']
        #fields = '__all__'