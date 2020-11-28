from .models import Article
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
)


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/detail_list.html'
    queryset = Article.objects.all()

    # a method to override pk in url and put id instead.
    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id=_id)
