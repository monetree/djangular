from django import forms
from django.forms import ModelForm
from .models import Angular

class AngularForm(forms.ModelForm):
    class Meta:
        model = Angular
        fields = '__all__'
