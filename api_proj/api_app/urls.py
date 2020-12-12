from django.urls.conf import path
from .views import article_list
from .models import Article

urlpatterns = [
    path('myapi/', article_list, name='myapi' ),
]
