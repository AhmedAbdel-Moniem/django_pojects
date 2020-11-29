from django.shortcuts import render
from django.views import View

# A class to convert a FBV 2 CBV.


class MyFunc(View):
    # Get method.
    def get(self, request, *args, **kwargs):
        return render(request, 'courses/rendered_template.html', {})


# HTTP Method
def my_func(request, *args, **kwargs):
    return render(request, 'courses/rendered_template.html', {})
