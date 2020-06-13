from django.shortcuts import render
from django.http import HttpResponse
from .models import Train

# Create your views here.
def my_view(request):
    training = Train.objects.order_by('first_name')
    return render(request,'templates/index.html', {'training':training})

def index(request,*args,**kwargs):
    return HttpResponse('<h1>hello world</h1>')