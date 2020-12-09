from django.shortcuts import render
from .models import My_API_Model
from django.http import JsonResponse


def my_api_view(request, *args, **kwargs):
    api_model = My_API_Model.objects.all()
    data = {'results': list(api_model.values('pk', 'api_name', 'api_details'))}
    return JsonResponse(data)
