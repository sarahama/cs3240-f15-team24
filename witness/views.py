from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth

from django.http import HttpResponse

# Create your views here.

def super(request):
    return render_to_response("witness/base_site.html", {'hello':"Hello World"})

def home(request):
    return render_to_response("witness/home.html", {'hello': "Hello World"})

#def login_view(request):
#    username = request.POST.get('username', '')
#    password = request.POST.get('password', '')
#    user = auth.authenticate(username=username, password = password)
#    if user is not None and user.is_active:
#        #correct password, user is active
#        auth.login(request, user)
#        #direct to success page
#        return HttpResponseRedirect("/account/loggedin")
#    else:
#        #error page
#        return HttpResponseRedirect("/account/invalid")
#        #return render_to_response("witness/login.html", {'hello':"Login here"})

#def loqout_view(request):
#    auth.logout(request)
#    return HttpResponseRedirect("/account/loggedout/")

#def register(request):
#    return render_to_response("witness/register.html", {'hello': "Register here"})
