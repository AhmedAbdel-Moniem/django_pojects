from django.urls.conf import path
from .views import article_list
from .models import Article

urlpatterns = [
    path('api', article_list, name='api' )
]
