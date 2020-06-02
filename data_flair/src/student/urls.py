from django.urls import path
from .views import student_show 
urlpatterns = [
    path('', student_show, name='student_show')
]