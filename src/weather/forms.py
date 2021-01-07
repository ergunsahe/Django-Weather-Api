from os import name
from django import forms
from django.forms import fields
from .models import City

class CityField(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CityForm(forms.ModelForm):
    name = CityField(label="", widget=forms.TextInput(attrs={'placeholder': 'Type a city name'}))
    class Meta:
        model = City
        fields = ("name",)