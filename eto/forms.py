from django.forms import ModelForm


from bl.models import BL
from lc.models import LC

class AddTerminalForm(ModelForm):
    class Meta:
        model = BL
        fields = ['terminal']

class AddPQAForm(ModelForm):
    class Meta:
        model = LC
        fields = ['pqaPayorder', 'bank', 'branch']