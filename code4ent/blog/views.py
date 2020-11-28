from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/detail_list.html'
    queryset = Article.objects.all() # this to filter the queryset if needed.

    # a method to override pk in url and put id instead.
    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id=_id)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = 'http://127.0.0.1:8003/blog/'

    def get_success_url(self):
        return 'http://127.0.0.1:8003/blog/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = 'http://127.0.0.1:8003/blog/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return 'http://127.0.0.1:8003/blog/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:article_list')

