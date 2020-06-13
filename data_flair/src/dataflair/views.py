from django.views.generic.base import RedirectView # Redirect Class Based
from django.http import HttpResponse
from django.shortcuts import render, redirect # Redirect Function Based
from django.contrib import sessions 

def index(request):
    return HttpResponse("<h1>Data Flair Django</h1>Hello, you just configured your First URL")
# Function Based Redirecting 
def data_flair(request):
    return redirect('/dataflair')
# Class Based Redirecting
class RedirectingClass(RedirectView):
    url='https://www.yahoo.com/'



# Set Cookies
def setcookie(request):
    html = HttpResponse("<h1>mycookie'()' function made by <i>'.set_cookie' </i>attribute</h1>")
    # Cookie with     Name,             Value ,                   max_age.
    html.set_cookie('mycookie', 'this is the value of my cookie', max_age=None)
    return html

# Get cookies by using the attribute {request.COOKIES[]}
def showcookie(request):  # cookie name
    show = request.COOKIES['mycookie']
    html = "<h1>SHOWCOOKIE'()' function to show the value of my cookie by 'request.COOKIES[]':  {}</h1>".format(show)
    return HttpResponse(html) 


# Advanced using request.COOKIES.get()
def setcookieagain(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

def showcookieagain(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse(
        "<h1>{0}<br>You have requested this page {1} times</h1>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookieagain')

# Deleting Cookies by response.delete_cookie()
def deletecookie(request):
    if request.COOKIES.get('visitors'):
        response = HttpResponse("<h1>Cookie Deleted</h1>")
        response.delete_cookie('visits')
    else:
        response = HttpResponse(
        "<h1>need to create cookie before deleting</h1>")
    return response


# Check if the browser supports and accept cookies to work with sessions.
def cookie_session(request):
    request.session.set_test_cookie() # tst cookie method works with every request.
    return HttpResponse('<h1>this is test cookie sessions</h1>')

def cookie_delete(request):
    if request.session.test_cookie_worked():# returns a boolean value as True after the browser 
                                            # accepts the cookie, Otherwise, it’s false.
        request.session.delete_test_cookie() # delete  the testcookie method.
        response = HttpResponse("<h2>cookie created</h2>")
        return response
    else:
        return HttpResponse('<h2> your browser does not accept cookie')



# Creating & Accessing Django Sessions
""" this this by {REQUEST} that has {SESSION} attribute that
CREATE, ACCESS and EDIT session variables, this attribute acts
as a dictionary as we define session names as keys and valuues as values """

# Create
def create_session(request):
    request.session['name'] = 'ahmed'
    request.session['password'] = 'xyz'
    return HttpResponse("<h1> Session is set</h1>")

# Aceess by get() method.
def access_session(request):
    response = "<h1> welcome to our session</h1>"
    if request.session.get('name'):
        response += "Name : {} ".format(request.session.get('name'))
       
    if request.session.get('password'):
        response += "<br>Password : {} ".format(request.session.get('password'))

        return HttpResponse(response)
    else:
        return redirect('/create')

# Delete
""" that does not delete the cookies in the browser 
but deleted from the database, to delete the cookies
completely we can use {flush()

Configuring Session Engine: 
Django lets you choose between these options but doesn’t limit your choices.
 If you want another storage method, you can find it on djangopackages.org
 1- DATABASE-BACKEND SESSION by {django.contrib.sessions}
 2- CASHES SESSION, setting up multile cashes{django.contrib.sessions.backends.cashe
 this used when needing persistent session data with servers, everything written to the cash and database too
 3- FILE BASED SESSION, store data in directory{django.contrib.sessions.backends.file
 , plz check if server has the permission to r/w the local directory
 4- COOKIE-BASED SESSION"""
def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse('<center><h1>Session Deleted</h1></center>')

