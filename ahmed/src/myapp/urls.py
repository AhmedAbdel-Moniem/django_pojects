from django.urls import path
from .views import HomePage, AboutPage



urlpatterns = [
    path('',HomePage.as_view(), name='home' ), # as_view() is used with the CBV
    path('about/', AboutPage.as_view(), name='about'), 
]