from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Raw
from .forms import RawForm


class CreateView(View):
    template_name = 'raws/create.html'

    def get(self, request, *args, **kwargs):
        form = RawForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RawForm(request.POST)
        if form.is_valid():
            form.save()
        form = RawForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class ListView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'raws/product_list.html'
        objects = Raw.objects.all()
        context = {'raws': objects}
        return render(request, template_name, context)


class DetailView(View):

    def get(self, request, id=None, *args, **kwargs):
        template_name = 'raws/product_detail.html'
        context = {}
        if id is not None:
            obj = get_object_or_404(Raw, id=id)
            context['objects'] = obj
        return render(request, template_name, context)


def fbv_view(request, *args, **kwargs):
    return render(request, 'raws/product_detail.html', {})


class CBV(View):

    def get(self, request, id=None, *args, **kwargs):
        template_name = 'raws/product_detail.html'
        context = {}
        return render(request, template_name, context)
