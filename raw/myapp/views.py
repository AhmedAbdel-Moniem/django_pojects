from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


class ProductDetailView(View):
    def get(self, request,id=None, *args, **kwargs):
        context = {}
        template_name = 'product_detail.html'
        if id is not None:
            obj = get_object_or_404(Product, id=id)
            context['object'] = obj
        return render(request, template_name, context)


class ProductListView(View):
    template_name = "product_list.html"
    queryset = Product.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    def get(self,request, *args, **kwargs):
        context = {'objects': self.get_queryset()}
        return render(request, self.template_name, context)        



def fbv_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

