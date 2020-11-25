from django import forms
from .models import Product


class MyForm(forms.ModelForm):
    title = forms.CharField()
    # email = forms.EmailField()
    hint = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Enter your hint',
        'class': 'my class',
        'id': 'my id',

    }))
    description = forms.CharField()
    summary = forms.CharField()
    price = forms.DecimalField(initial=2.2, max_digits=3, decimal_places=2)

    class Meta:
        model = Product
        fields = ['title', 'hint', 'description', 'summary', 'price']

    def clean_hint(self):
        hint = self.cleaned_data.get('hint')
        if 'ahmed' in hint:
            raise forms.ValidationError('Delete Ahmed plz')
        return(hint)

# class MyForm2(forms.Form):
#     title = forms.CharField()
#     # email = forms.EmailField(initial='ahmed.moname@gmail.com')
#     hint = forms.CharField(required=True, widget=forms.Textarea(attrs={
#         'placeholder': 'your hint',
#         'class': 'my class',
#         'id': 'my id',
#
#
#     }))
#     description = forms.CharField()
#     summary = forms.CharField()
#     price = forms.DecimalField(initial=2.22, max_digits=3, decimal_places=2)
