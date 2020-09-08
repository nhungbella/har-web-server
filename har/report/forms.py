from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Report

class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-common'
            if field_name == 'username':
                field.widget.attrs['class'] = 'form-username'

        
class CreateUserForm(PlaceholderMixin, UserCreationForm):
    password2 = None
    class Meta:
        model = User
        fields = ['username', 'password1']        


class ReportForm(PlaceholderMixin, forms.ModelForm):
    name = forms.CharField(label='Report name')
    class Meta:
        model = Report
        fields = [
            'name',
            'longitude',
            'latitude',
            'altitude',
            'accuracy',
        ]