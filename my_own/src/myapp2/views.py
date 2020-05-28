from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request, *args, **kwargs):
	
	return HttpResponse("<h1> injected html phrase</h1>")



def contact(request, *args, **kwargs):
	
	return HttpResponse("<h1> Contact Page</h1>")