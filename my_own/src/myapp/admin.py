from django.contrib import admin

# Register your models here.
from .models import my_model_app 
admin.site.register(my_model_app)