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
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from .forms import CreateGroupForm, AddGroup
from .forms import MessageF
from .models import MessageM
from django.forms import ModelForm
from django.forms import formset_factory
from django.db import models
from report.models import Report

from django.forms import ModelForm

# Create your views here.

def super(request):
    return render_to_response("witness/base_site.html", {'hello':"Hello World"})

def home(request):
    return render_to_response("witness/home.html", {'hello': "Hello World"})

def userpage(request):
    #username = get_object_or_404(Reporter, pk=name)
    #return render(request, 'witness/userpage.html')
    context = RequestContext(request)
    addGroup = AddGroup()
    return render_to_response('witness/userpage.html', {'addGroup':addGroup}, context)

def user_reports(request):
    context = RequestContext(request)
    if request.method == 'POST':
        search = request.POST.get('search', '')
        reports = Report.objects.filter(report_title__contains = search, report_owner__exact = request.user)
        return render_to_response('witness/user_reports.html', {'reportList':reports}, context)
    else:
        reports = Report.objects.filter(report_owner__exact = request.user)
        return render_to_response('witness/user_reports.html', {'reportList':reports}, context)

def user_view_report(request):
    context = RequestContext(request)
    if request.method == 'GET':
        reportTitle = request.GET.get("view", '')
        report = Report.objects.get(report_title = reportTitle)
        reportTitle = report.report_title
        reportShort = report.report_short_description
        reportLong = report.report_long_description
        created = report.report_creation_date
        owner = report.report_owner
        public = report.report_public
        return render_to_response('witness/admin_view_report.html', {'reportTitle': reportTitle,
        'reportShort': reportShort, 'reportLong':reportLong, 'created':created, 'owner': owner, 'public':public}, context)
    else:
        reports = Report.objects.all()
        return render_to_response('witness/admin_reports.html', {'reportList':reports}, context)
    
def addgroup(request):
    context = RequestContext(request)
    if request.method == 'POST':
        for group in request.user.groups.all():
            if group.name == request.POST.get('name',''):
                for user in User.objects.all():
                    if user.username == request.POST.get('member',''):
                        user.groups.add(group)
        return HttpResponseRedirect("/userpage")
    else:
        addGroup = AddGroup()
        return render_to_response('witness/addgroup.html', {'addGroup':addGroup}, context)

def grouphome(request):
    context = RequestContext(request)
    if request.method == 'POST':
        pass
    else:
        return render_to_response('witness/grouphome.html', context)
	
def creategroup(request):
    context = RequestContext(request)
    if request.method == 'POST':
        group = Group.objects.create(name=request.POST.get('name',''))
        group.save()
        request.user.groups.add(group)
        group.save()
        return HttpResponseRedirect("/userpage")
    else:
        newForm = CreateGroupForm()
        return render_to_response('witness/creategroup.html', {'newForm':newForm}, context)

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password = password)
        if user is not None and user.is_active:
            #correct password, user is active
            auth.login(request, user)
            #direct to success page
            return HttpResponseRedirect("/userpage")
        else:
            #error page
            #return HttpResponseRedirect("/account/invalid")
            return render_to_response("witness/login.html", {'hello':"Login here"})
    return render_to_response("witness/login.html", RequestContext(request, {}))

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


def access_error(request):
    return render_to_response('witness/no_access.html')

def registration_success(request):
    return render_to_response('witness/registration_success.html')


def admin_home(request):
    if request.user.is_superuser:
        return render_to_response('witness/admin_home.html')    
    else:
        return render_to_response('witness/no_access.html')

def admin_users(request):
    context = RequestContext(request)
    if request.method == 'POST':	
        search = request.POST.get('search', '')
        reporters = Reporter.objects.filter(name__contains = search)
        return render_to_response('witness/admin_reporters.html', {'reporterList':reporters}, context)
    else:
        reporters = Reporter.objects.all()
        return render_to_response('witness/admin_reporters.html', {'reporterList':reporters}, context)

def admin_reports(request):
    context = RequestContext(request)
    if request.method == 'POST':
        search = request.POST.get('search', '')
        reports = Report.objects.filter(report_title__contains = search)
        return render_to_response('witness/admin_reports.html', {'reportList':reports}, context)
    else:
        reports = Report.objects.all()
        return render_to_response('witness/admin_reports.html', {'reportList':reports}, context)

def admin_view_report(request):
    context = RequestContext(request)
    if request.method == 'GET':
        reportTitle = request.GET.get("view", '')
        report = Report.objects.get(report_title = reportTitle)
        reportTitle = report.report_title
        reportShort = report.report_short_description
        reportLong = report.report_long_description
        created = report.report_creation_date
        owner = report.report_owner
        public = report.report_public
        return render_to_response('witness/admin_view_report.html', {'reportTitle': reportTitle,
        'reportShort': reportShort, 'reportLong':reportLong, 'created':created, 'owner': owner, 'public':public}, context)
    else:
        reports = Report.objects.all()
        return render_to_response('witness/admin_reports.html', {'reportList':reports}, context)

def admin_edit_user(request):
    context = RequestContext(request)
    if request.method == 'GET':
        reporterName = request.GET.get('edit','')
        reporter = Reporter.objects.get(name = reporterName)
        user = User.objects.get(username = reporterName)
        form = ReporterForm(instance = reporter)
        form2 = UserEditForm(instance = user)
        return render_to_response('witness/admin_edit_user.html', { 'reporterName': reporterName, 'form': form, 'form2':form2}, context)
    elif request.method == 'POST':
        reporterName = request.POST.get("save")
        reporter = Reporter.objects.get(name = reporterName)
        reporter.name = request.POST.get('name', '')
        reporter.user.username = request.POST.get('name', '')
        reporter.user.groups = request.POST.get('groups', '')
        reporter.user.is_active = request.POST.get('is_active', '')
        reporter.user.is_superuser = request.POST.get('is_superuser', '')
        reporter.save()
        reporter.user.save()
        return render_to_response('witness/admin_edit_user.html', {'response':'User updated successfully'}, context)
    else:
        return render_to_response('witness/no_access.html')

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['name']

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['groups', 'is_active', 'is_superuser']

def get_Message(request):
    if request.method == 'POST':
        message1 = MessageF(request.POST)
        if message1.is_valid():
            author = request.POST.get('author', '')
            message = request.POST.get('message','')
            newmsg = MessageM(author = author, message = message)
            newmsg.save()
            results = MessageM.objects.all()
            #messagetest = message.save()
            #return HttpResponse('Done')
            return render(request, 'witness/messaging2.html', {'author': author, 'message': message})
    else:
        message = MessageF()
        return render(request, 'witness/messaging.html', {'message': message})        




