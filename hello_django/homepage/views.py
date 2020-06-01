from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomepageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs): # built in standard django function to add data to templates.
        # a function to inject python objects, functions, num or whatever inside html <p>{{ my_statement }}
        context = super().get_context_data(**kwargs)
        context['my_statement'] = "Nice To See You"
        return context
    
    # method to call from html
    def say_bye(self):
        return 'Good bye'