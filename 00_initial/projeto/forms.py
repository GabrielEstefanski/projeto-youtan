from django import forms
from .crm.models import Cnpj

class Cnpj(forms.ModelForm):
    class Meta:
        model = Cnpj
        fields = ('cnpj', 'cidade')