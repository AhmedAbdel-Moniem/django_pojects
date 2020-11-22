from django.shortcuts import render
from .models import Product
from .forms import MyForm, MyForm2


def my_main_page(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {'object': obj}
    return render(request, 'product/home.html', context)


def about_page(request, *args, **kwargs):
    context = {}
    return render(request, 'product/about.html', context)

def myform_view(request):
    form = MyForm2()
    if request.method == 'POST':
        form = MyForm2(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
            form = MyForm2
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'product/my_form.html', context)
# Model Form
# def myform_view(request):
#     form = MyForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = MyForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'product/my_form.html', context)


# # Django Pure Form
# def myform2_view(request):
#     my_form = MyForm2()
#     if request.POST == 'POST':
#         my_form = MyForm2(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, 'product/form_two.html', context)
