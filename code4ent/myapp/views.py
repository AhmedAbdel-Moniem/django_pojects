from django.shortcuts import render

from .forms import MyForm

from .models import Product


# def render_initial_data(request):
#     initial_data = {
#         'title': 'this is my title',
#         'summary': 'this is my summary'
#     }
#     obj = Product.objects.get(id=6)
#     form = MyForm(request.POST or None, initial_data, instance=obj)
#     if form.is_valid():
#         form.objects.create(**form.cleaned_data)
#         form = MyForm()
#     context = {'form': form}
#
#     return render(request, 'product/my_form.html', context)


def my_main_page(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {'object': obj}
    return render(request, 'product/home.html', context)


def about_page(request, *args, **kwargs):
    context = {}
    return render(request, 'product/about.html', context)


def myform_view(request):
    initial_data = {
        'title': 'this is my title',
        'summary': 'this is my summary'
    }
    obj = Product.objects.get(id=6)

    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST or None, initial_data, instance=obj)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
            form = MyForm
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'product/my_form.html', context)


# def myform_view(request):
#     form = MyForm2()
#     if request.method == 'POST':
#         form = MyForm2(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#             form = MyForm2
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, 'product/my_form.html', context)
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
def dynamic_url_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {'objects': obj}
    return render(request, 'product/product_detail.html', context)
