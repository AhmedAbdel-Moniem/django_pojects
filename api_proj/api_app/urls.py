from django.urls.conf import path
from .views import article_list, article_detail
from .models import Article
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #function api
    path('fapi/', article_list),
    path('fapi/<int:pk>/', article_detail),
]
# function api
urlpatterns = format_suffix_patterns(urlpatterns)