from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields + ('age',)
        fields = ('username', 'email','age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email','age',)