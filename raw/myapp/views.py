from django.shortcuts import render
from django.views import View


class From_Fbv_2_Cbv(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

def fbv_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

