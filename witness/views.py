from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.template import RequestContext
from .models import Reporter
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import GroupForm

# Create your views here.

def super(request):
    return render_to_response("witness/base_site.html", {'hello':"Hello World"})

def home(request):
    return render_to_response("witness/home.html", {'hello': "Hello World"})

def userpage(request):
    #username = get_object_or_404(Reporter, pk=name)
    return render(request, 'witness/userpage.html')
	
def creategroup(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return render_to_response("witness/userpage.html")
    else:
        newForm = GroupForm()
        return render_to_response('witness/creategroup.html', {'newForm':newForm}, context)

def login(request):
    return render_to_response("witness/login.html", {'hello':"Login here"})
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password = password)
    if user is not None and user.is_active:
        #correct password, user is active
        auth.login(request, user)
        #direct to success page
        return HttpResponseRedirect("/userpage.html")
    else:
        #error page
        return HttpResponseRedirect("/account/invalid")
        return render_to_response("witness/login.html", {'hello':"Login here"})

def logout(request):
    auth.logout(request)
    return render_to_response("witness/logout.html")

def register(request):
    if request.method == 'POST':    
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        user = User.objects.create_user(username=username,email=email, password = password)
        user = authenticate(username=username, password = password)
        #user.save()
        if user is not None and user.is_active:
            #correct password, user is active
            #create a reporter with the user and log the user in
            reporter = Reporter(name = username, user = user)
            reporter.save()
            auth.login(request, reporter.user)
            #direct to success page
            return HttpResponseRedirect("/userpage")
        else:
            #error page
            return HttpResponseRedirect("/account/invalid")
            #return render_to_response("witness/login.html", {'hello':"Login here"})
    else:
        return render_to_response("witness/register.html", RequestContext(request, {}))


def registration_success(request):
    return render_to_response('witness/registration_success.html')

#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            new_user = form.save()
#            return HttpResponseRedirect("/books/")
#    else:
#        form = UserCreationForm()
#    return render(request, "registration/register.html", {
#        'form': form,
#    })



