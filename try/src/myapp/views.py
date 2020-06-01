from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = "index.html"
    # default Django function to inject python objects in html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = "Hello, World!"
        return context
        
    def hello(self):
        return 'hello'
