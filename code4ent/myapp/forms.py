from django import forms
from .models import Product


class MyForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'hint', 'description', 'summary']


class MyForm2(forms.Form):
    title = forms.CharField()
    hint = forms.CharField()
    price = forms.DecimalField()
