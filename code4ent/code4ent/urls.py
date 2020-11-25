"""code4ent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import my_main_page, about_page,myform_view, dynamic_url_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_main_page, name='home'),
    path('about/', about_page, name='about'),
    path('create_form/', myform_view, name='create_form'),
    # path('create_form2/', render_initial_data, name='create_form2'),
    path('product/<int:my_id>', dynamic_url_view, name='dynamic_url')
]
