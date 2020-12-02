from django.forms import ModelForm
from .models import Raw


class RawForm(ModelForm):
    class Meta:
        model = Raw
        fields = ['title']
