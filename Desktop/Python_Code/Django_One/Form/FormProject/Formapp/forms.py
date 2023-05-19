from django import forms
from .models import Formapp

class FormappForm(forms.ModelForm):
    class Meta:
        model = Formapp
        fields = ['Name', 'Message']