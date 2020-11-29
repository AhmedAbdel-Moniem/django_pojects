from django.urls import path
from .views import my_func, MyFunc

app_name = 'courses'
urlpatterns = [
    path('fbv', my_func, name='fbv'),
    path('cbv', MyFunc.as_view(), name='cbv'),
]