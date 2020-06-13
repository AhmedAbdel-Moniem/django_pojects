from django.urls import path
from .views import my_view, index

urlpatterns = [
    path('', my_view, name='my_view'),
    path('i/', index)
]