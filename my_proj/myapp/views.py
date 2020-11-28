from .models import Product

def home_view(request, *args, **kwargs):
	""" this is my doc string"""
    model = Product
    context = {}
    return render(request, 'about.html', context)
