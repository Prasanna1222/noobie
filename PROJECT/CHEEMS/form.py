from django import forms
from CHEEMS.models import customerModel
from CHEEMS.models import dogModel
class customerForm(forms.ModelForm):
    class Meta:
        model=customerModel
        fields="__all__"
class dogForm(forms.ModelForm):
    class Meta:
        model=dogModel
        fields="__all__"