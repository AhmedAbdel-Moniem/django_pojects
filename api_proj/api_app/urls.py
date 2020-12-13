from django.urls.conf import path
from .views import article_list, article_detail
from .models import Article

urlpatterns = [
    path('myapi/', article_list),
    path('myapi/<int:pk>/', article_detail),
]
