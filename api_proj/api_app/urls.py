from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    article_list,
    article_detail,
    ArticleList,
    ArticleDetail,

    ArticleDetailMixin,
    ArticleListMixins,

    ArticleDetailGeneric,
    ArticleListGeneric,
)


urlpatterns = [
    # function api
    path('fapi/', article_list),
    path('fapi/<int:pk>/', article_detail),

    # class apis
    path('capi/', ArticleList.as_view()),
    path('capi/<int:pk>/', ArticleDetail.as_view()),

    path('mcapi/', ArticleListMixins.as_view()),
    path('mcapi/<int:pk>/', ArticleDetailMixin.as_view()),

    path('gcapi/', ArticleListGeneric.as_view()),
    path('gcapi/<int:pk>/', ArticleDetailGeneric.as_view()),

]
# function api
urlpatterns = format_suffix_patterns(urlpatterns)
