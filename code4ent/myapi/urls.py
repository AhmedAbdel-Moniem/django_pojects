from django.urls import path
from .views import my_api_view
app_name = 'myapi'
urlpatterns = [
    path('', my_api_view, name='api'),
]
