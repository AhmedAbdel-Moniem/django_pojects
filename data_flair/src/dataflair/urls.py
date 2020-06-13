"""dataflair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    #Function Based Redirecting
    path('redirect/', data_flair),
    path('dataflair/', index),
    
    #  Built-In Class Based Redirecting
    path('google/', RedirectView.as_view(url="https://www.google.com")),
    # Class Based Redirecting
    path('yahoo/',RedirectingClass.as_view()),
    
    # Simple Cookies
    path('setcookie/', setcookie),
    path('showcookie/', showcookie),

    # Advanced using request.COOKIES.Get()
    path('setcookieagain/', setcookieagain),
    path('showcookieagain/', showcookieagain),
    
    # check supporting cookie by browser to work with sessions.
    path('cookiesession/', cookie_session),
    path('cookiedelete/', cookie_delete),

    # Creating & Accessing& Delete SESSION.
    path('create/', create_session),
    path('access/', access_session),
    path('delete/', delete_session),

 ]
