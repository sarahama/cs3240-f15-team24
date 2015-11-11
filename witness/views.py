from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader


from django.http import HttpResponse

# Create your views here.

def super(request):
    return render_to_response("witness/base_site.html", {'hello':"Hello World"})

def home(request):
    return render_to_response("witness/home.html", {'hello': "Hello World"})

def userpage(request):
    #return HttpResponse("Welcome User")
    template = loader.get_template('witness/userpage.html')
    return render(request, 'witness/userpage.html')

def login(request):
    return render_to_response("witness/login.html", {'hello':"Login here"})
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password = password)
    if user is not None and user.is_active:
        #correct password, user is active
        auth.login(request, user)
        #direct to success page
        return HttpResponseRedirect("/witness/userpage.html")
    else:
        #error page
        return HttpResponseRedirect("/account/invalid")
        return render_to_response("witness/login.html", {'hello':"Login here"})

def logout(request):
    auth.logout(request)
    return render_to_response("witness/logout.html")

def register(request):
    return render_to_response("witness/register.html", {'hello': "Register here"})
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    reporter = Reporter.user.objects.create_user(username=username,email=email, password = password)
    reporter.save()
    if user is not None and user.is_active:
        #correct password, user is active
        auth.login(request, user)
        #direct to success page
        #return HttpResponseRedirect("/account/loggedin")
    else:
        #error page
        return HttpResponseRedirect("/account/invalid")
        #return render_to_response("witness/login.html", {'hello':"Login here"})






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



