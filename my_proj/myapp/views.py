from django.shortcuts import render
from .models import Product

def home_view(request, *args, **kwargs):
    model = Product
    context = {}
    return render(request, 'about.html', context)