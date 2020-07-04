from django.views.generic import TemplateView # it makes everything for us

# Class based view

class HomePage(TemplateView):
    template_name = 'home.html'  # all we need with this class is the template name or html file.

class AboutPage(TemplateView):
    template_name = 'about.html'