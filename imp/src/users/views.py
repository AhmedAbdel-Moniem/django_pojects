from django.urls import reverse_lazy
from .forms import CusomUserCreationForm
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = CusomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
