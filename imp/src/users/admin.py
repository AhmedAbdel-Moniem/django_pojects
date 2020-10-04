from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CusomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    new_form = CusomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','nationality','age','is_staff']

    def __str__(self):
        return self.text

admin.site.register(CustomUser, CustomUserAdmin)