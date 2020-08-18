from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
