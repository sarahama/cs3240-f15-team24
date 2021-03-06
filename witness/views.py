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
from report.models import File
from django.views.generic.edit import UpdateView
from django.forms import ModelForm
#from .ecryption import encrypt
#from .ecryption import decrypt
from report.forms import ReportForm
from report.models import ReportFolder
from itertools import chain
from Crypto.PublicKey import RSA
import base64
from base64 import b64decode
import smtplib
from email.mime.text import MIMEText
from .forms import AddMember
from report.forms import ReportForm
from report.models import ReportFolder
from itertools import chain
import json
from django.http import JsonResponse


from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random
import sys

from Crypto.Cipher import DES
import os


# Create your views here.

def super(request):
    return render_to_response("witness/base_site.html", {'hello':"Hello World"})

def home(request):
    return render_to_response("witness/home.html", {'hello': "Hello World"})

def userpage(request):
    #username = get_object_or_404(Reporter, pk=name)
    #return render(request, 'witness/userpage.html')
    results = MessageM.objects.all()
    count = 0
    for i in results:
        if request.user.username == i.reader:
            count+=1
    results = count
    context = RequestContext(request)
    addGroup = AddGroup()
    return render_to_response('witness/userpage.html', {'addGroup':addGroup, 'results':results}, context)

def user_reports(request):
    context = RequestContext(request)
    if request.method == 'POST':
        if request.POST.get('filter','') == 'go':
            reports = []
            if request.POST.get('myreports',''):
                reports = Report.objects.filter(report_owner__exact = request.user)
            all_reports = Report.objects.all()
            access = []
            for report in all_reports:
                group_name = report.report_group
                #add the report if the user is an a group that can view the report
                if request.POST.get('groupaccess',''):
                    if request.user.groups.filter(name = group_name).exists() and report not in reports:
                        access.append(report) 
                #add the report if it is public
                if request.POST.get('public',''):
                    if report.report_public and report not in reports and report not in access:
                        access.append(report)
            final = list(chain(reports, access))
            return render_to_response('witness/user_reports.html', {'reportList':final}, context)
        else:
            search = request.POST.get('search', '')
            reports = Report.objects.filter(report_title__contains = search, report_owner__exact = request.user)
            all_reports = Report.objects.filter(report_title__contains = search)
            access = []
            for report in all_reports:
                group_name = report.report_group
                for r in reports:
                    if r not in access:
                        access.append(r)
                #add the report if the user is an a group that can view the report
                if request.user.groups.filter(name = group_name).exists() and report not in reports:
                    access.append(report) 
                #add the report if it is public
                if report.report_public and report not in reports and report not in access:
                    access.append(report)

            reports_short = Report.objects.filter(report_short_description__contains = search, report_owner__exact = request.user)
            all_reports_short = Report.objects.filter(report_short_description__contains = search)
            for report in all_reports_short:
                group_name = report.report_group
                for r in reports_short:
                    if r not in access:
                        access.append(r)
                if request.user.groups.filter(name = group_name).exists() and report not in reports_short:
                    access.append(report) 
                if report.report_public and report not in reports_short and report not in access:
                    access.append(report)

            reports_location = Report.objects.filter(report_location__contains = search, report_owner__exact = request.user)
            all_reports_location = Report.objects.filter(report_location__contains = search)
            for report in all_reports_location:
                group_name = report.report_group
                for r in reports_location:
                    if r not in access:
                        access.append(r)
                if request.user.groups.filter(name = group_name).exists() and report not in reports_location:
                    access.append(report) 
                if report.report_public and report not in reports_location and report not in access:
                    access.append(report)
            final = list(chain(reports, access))
            return render_to_response('witness/user_reports.html', {'reportList':final}, context)
    else:
        reports = Report.objects.filter(report_owner__exact = request.user)
        all_reports = Report.objects.all()
        access = []
        for report in all_reports:
            group_name = report.report_group
            #add the report if the user is an a group that can view the report
            if request.user.groups.filter(name = group_name).exists() and report not in reports:
                access.append(report)
            #add the report if it is public
            if report.report_public and report not in reports and report not in access:
                access.append(report)
        final = list(chain(reports, access))
        return render_to_response('witness/user_reports.html', {'reportList':final}, context)

def user_view_report(request):
    context = RequestContext(request)
    if request.method == 'GET':
        #reportTitle = request.GET.get("view", '')
        report_pk = request.GET.get("view",'')
        report = Report.objects.get(pk = report_pk)
        files = report.report_files.split(',')
        file_list = []
        for f in files:
            if f != '':
                if File.objects.filter(pk__exact = int(f)).exists():
                    f2 = File.objects.get(pk = int(f))
                    file_list.append(f2)
        return render_to_response('witness/admin_view_report.html', {'report': report, 'file_list':file_list}, context)
    else:
        reports = Report.objects.filter(report_owner__exact = request.user)
        return render_to_response('witness/user_reports.html', {'reportList':reports}, context)

def deleted_report(request):
    context = RequestContext(request)
    if request.method == 'POST':
        report_pk = request.POST.get('delete', '')
        report = Report.objects.get(pk = report_pk)
        reportTitle = report.report_title
        report.delete()
        return render_to_response('reports/deleted_report.html', {'reportTitle':reportTitle}, context)


def user_folders(request):
    context = RequestContext(request)
    if request.method == 'POST' and request.POST.get('delete', '') != '':
        deletefolder = request.POST.get('delete', '')
        folder = ReportFolder.objects.get(pk = deletefolder)
        folder.delete()
        folders = ReportFolder.objects.filter(folder_owner__exact = request.user)
        return render_to_response('witness/user_folders.html', {'folderList':folders}, context)
    elif request.method == 'POST':
        search = request.POST.get('search', '')
        folders = ReportFolder.objects.filter(folder_title__contains = search, folder_owner__exact = request.user)
        return render_to_response('witness/user_folders.html', {'folderList':folders}, context)
    else:
        folders = ReportFolder.objects.filter(folder_owner__exact = request.user)
        return render_to_response('witness/user_folders.html', {'folderList':folders}, context)
    
def user_view_folders(request):
    context = RequestContext(request)
    invalid_report = False
    if request.method == 'GET':
        folder_pk = request.GET.get("view", '')
        folder = ReportFolder.objects.get(pk = folder_pk)
        folderTitle = folder.folder_title
        reports = folder.folder_reports
        report_list2 = []
        if reports != '':
            report_list = reports.split(',')
            for report in report_list:
                if report != '':
                    if Report.objects.filter(pk__exact = report).exists():
                        report_inst = Report.objects.get(pk = report)
                        report_list2.append(report_inst)
                    else:
                        folder.folder_reports = folder.folder_reports.replace(report, '', 1)
        return render_to_response('witness/user_view_folders.html', {'folder': folder, 'reportList':report_list2}, context)
    elif request.method == 'POST' and request.POST.get('edit2', '') != '':
        addreport = request.POST.get('addreport','')
        folder_pk = request.POST.get('edit2', '')
        remove = request.POST.get('removereport','')
        folder = ReportFolder.objects.get(pk = folder_pk)
        report_list = folder.folder_reports.split(',')
        if Report.objects.filter(report_owner__exact = request.user).filter(report_title__exact = addreport).exists():
            report = Report.objects.get(report_owner__exact = request.user, report_title__exact = addreport)
            report_pk = report.pk
            folder.folder_reports = folder.folder_reports + ',' + (str)(report_pk)
            folder.save()
        elif addreport != '':    
            invalid_report = True
        if Report.objects.filter(report_owner__exact = request.user).filter(report_title__exact = remove).exists():
            report = Report.objects.get(report_owner__exact = request.user, report_title__exact = remove)
            report_pk = str(report.pk)
            if report_pk in report_list:
                folder.folder_reports = folder.folder_reports.replace(report_pk, '', 1)
                folder.save()
        report_list2 = []
        reports = folder.folder_reports
        if reports != '':
            report_list = reports.split(',')
            for report in report_list:
                if report != '':
                    if Report.objects.filter(pk = int(report)).exists():
                        report_inst = Report.objects.get(pk = int(report))
                        report_list2.append(report_inst)
                    else:
                        folder.folder_reports = folder.folder_reports.replace(report, '', 1)
        return render_to_response('witness/user_view_folders.html', {'folder': folder, 'reportList':report_list2, 'invalid_report':invalid_report, 'report_name':addreport}, context)
    elif request.method == 'POST' and request.POST.get('rename','') != '':
        folderTitle = request.POST.get('rename', '')
        folder = ReportFolder.objects.get(folder_title = folderTitle, folder_owner__exact = request.user)
        newName = request.POST.get('renamefolder', '')
        if not ReportFolder.objects.filter(folder_title = newName).filter(folder_owner = request.user).exists() or newName == folderTitle:
            folder.folder_title = newName
            folder.save()
            #display the updated folder
            folderTitle = folder.folder_title
            reports = folder.folder_reports
            report_list2 = []
            if reports != '':
                report_list = reports.split(',')
                for report in report_list:
                    if report != '':
                        if Report.objects.filter(pk = int(report)).exists():
                            report_inst = Report.objects.get(pk = int(report))
                            report_list2.append(report_inst)
                        else:
                            folder.folder_reports = folder.folder_reports.replace(report, '', 1)

            return render_to_response('witness/user_view_folders.html', {'folder': folder, 'reportList':report_list2}, context)
        else:
            reports = folder.folder_reports
            report_list2 = []
            if reports != '':
                report_list = reports.split(',')
                for report in report_list:
                    if report != '':
                        if Report.objects.filter(pk = int(report)).exists():
                            report_inst = Report.objects.get(pk = int(report))
                            report_list2.append(report_inst)
                        else:
                            folder.folder_reports = folder.folder_reports.replace(report, '', 1)
            return render_to_response('witness/user_view_folders.html', {'folder': folder, 'reportList':report_list2, 'invalid_name':True}, context)
    else:
        folders = ReportFolder.objects.filter(folder_owner__exact = request.user)
        return render_to_response('witness/user_folders.html', {'folderList':folders}, context)


# def addgroup(request):
#     context = RequestContext(request)
#     added = False
#     if request.method == 'POST':
#         for group in request.user.groups.all():
#             if group.name == request.POST.get('name',''):
#                 added = True
#                 for user in User.objects.all():
#                     if user.username == request.POST.get('member',''):
#                         user.groups.add(group)
#         for group in Group.objects.all():
#             if group.name == request.POST.get('name',''):
#                 if request.user.is_superuser == True and added == False:
#                     for user in User.objects.all():
#                         if user.username == request.POST.get('member',''):
#                             user.groups.add(group)
#         return HttpResponseRedirect("/userpage")
#     else:
#         addGroup = AddGroup()
#         return render_to_response('witness/addgroup.html', {'addGroup':addGroup}, context)

def grouphome(request):
    context = RequestContext(request)
    if request.method == 'POST':
        pass
    else:
        groups = []
        if request.user.is_superuser:
            groups = Group.objects.all()
        return render_to_response('witness/grouphome.html', {'groups':groups}, context)
	
def user_view_group(request):
    context = RequestContext(request)
    if request.method == 'GET':
        name = request.GET.get('view','')
        group = Group.objects.get(name = name)
        users = group.user_set.all()
        reports = []
        if Report.objects.filter(report_group__exact = name).exists():
            reports = Report.objects.filter(report_group__exact = name)
        form = AddMember()
        return render_to_response('witness/user_view_group.html', {'group':group, 'users':users, 'reports':reports, 'form':form}, context)
    if request.method == 'POST':
        name = request.POST.get('view','')
        group = Group.objects.get(name = name)
        for user in User.objects.all():
            if user.username == request.POST.get('member',''):
                user.groups.add(group)
        users = group.user_set.all()
        reports = []
        if Report.objects.filter(report_group__exact = name).exists():
            reports = Report.objects.filter(report_group__exact = name)
        form = AddMember()
        return render_to_response('witness/user_view_group.html', {'group':group, 'users':users, 'reports':reports, 'form':form}, context)


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
    context = RequestContext(request) 
    private_key = ''
    if request.method == 'POST': 
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        userExists = User.objects.filter(username = username).exists()
        username_error = userExists
        if (username_error): #if there already exists a user with that name
            return render_to_response("witness/register.html", {'username_error': username_error}, context)

        elif(password2 == password):
            #pub_key = key1.publickey()
            user = User.objects.create_user(username=username,email=email, password = password)
            user = authenticate(username=username, password = password)
            #user.save()
            if user is not None and user.is_active:
                #correct password, user is active
                #create a reporter with the user and log the user in
                #generate their key for encrypting and decrypting
                random_generator = Random.new().read
                key = RSA.generate(1024, random_generator)
                private_key = key.exportKey() #this will be displayed
                #key = RSA.generate(2048)
                #f = open('mykey.txt','wb')
                #f.write(key.exportKey())
                #f.close()
                public_key = key.publickey().exportKey() #this will be saved
                reporter = Reporter(name = username, user = user, public_key = public_key)
                reporter.save()
                auth.login(request, reporter.user)
                #s = smtplib.SMTP('localhost')
                #s.sendmail("rtb7rd@virginia.edu", "rtb7rd@virginia.edu", "Hello")
                #s.quit()
                #direct to success page
                return render_to_response("witness/userpage.html", {'private_key':private_key, 'firstTime':True}, context)
            else:
                return HttpResponseRedirect("/account/invalid")
                
        else:
            password_error = True
            return render_to_response("witness/register.html", {'password_error': password_error, 'username':username, 'email':email}, context)
    else:
        password_error = False
        return render_to_response("witness/register.html", {'password_error': password_error}, context)


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
        report_pk = request.GET.get("view", '')
        report = Report.objects.get(pk = report_pk)
        files = report.report_files.split(',')
        file_list = []
        for f in files:
            if f != '':
                if File.objects.filter(pk__exact = int(f)).exists():
                    f2 = File.objects.get(pk = int(f))
                    file_list.append(f2)
        return render_to_response('witness/admin_view_report.html', {'report': report, 'file_list':file_list}, context)
    else:
        reports = Report.objects.all()
        return render_to_response('witness/admin_reports.html', {'reportList':reports}, context)



def admin_edit_user(request):
    context = RequestContext(request)
    response = ''
    if request.method == 'GET':
        reporterName = request.GET.get('edit','')
        reporter = Reporter.objects.get(name = reporterName)
        user = User.objects.get(username = reporterName)
        form = ReporterForm(instance = reporter)
        form2 = UserEditForm(instance = user)
        return render_to_response('witness/admin_edit_user.html', { 'reporterName': reporterName, 'form': form, 'form2':form2, 'response':response}, context)
    elif request.method == 'POST':
        reporterName = request.POST.get("save")
        reporter = Reporter.objects.get(name = reporterName)
        #reporter.name = request.POST.get('name', '')
        #reporter.user.username = request.POST.get('name', '')
        #reporter.user.groups = request.POST.get('groups', '')
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
        fields = []

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['is_active', 'is_superuser']

def get_Message(request):
    if request.method == 'POST':
        reader = request.POST.get('reader', '')
        message = request.POST.get('message','')
        username = request.user.username
        if request.POST.get('encmsg','') == "true":
            #username = request.user.username
            reporter = Reporter.objects.get(name = reader) #gets the public key of the reader
            key = reporter.public_key
            #translate back into an RSA public key
            public_key = RSA.importKey(key)
            #encode the message
            enc_data = secret_string(message, public_key)
            message = base64.b64encode(enc_data)
            print(message)
         
        newmsg = MessageM(reader = reader, message = message, author = username)
        newmsg.save()
        results = MessageM.objects.all()
        return render(request, 'witness/messaging2.html', {'reader': reader, 'message': message, 'results': results, 'username':username})
    else:
        message = MessageF()
        return render(request, 'witness/messaging.html', {'message': message})            

def user_edit_report(request):
    context = RequestContext(request)
    if request.method == 'GET':
        report_pk = request.GET.get('edit','')
        report = Report.objects.get(pk = report_pk)
        form = ReportEditForm(instance = report)
        return render_to_response('witness/user_edit_report.html', {'form':form, 'report':report}, context)
    elif request.method == 'POST':
        group_name = request.POST.get('report_group', '')
        groupExists = Group.objects.filter(name = group_name).exists()
        if groupExists or group_name == '':
            report_pk = request.POST.get("save")
            report = Report.objects.get(pk = report_pk)
            newName = request.POST.get('report_title', '')
            report.report_title = newName
            report.report_short_description = request.POST.get('report_short_description', '')
            report.report_long_description = request.POST.get('report_long_description', '')
            report.report_public = request.POST.get('report_public', '')
            #report.report_file_encryption = request.POST.get('report_file_encryption', '')
            #report.report_file = request.POST.get('report_file', '')
            report.report_group = request.POST.get('report_group', '')
            report.save()
            return render_to_response('witness/user_edit_report.html', {'response':'Report updated successfully'}, context)
        else:
            report_pk = request.POST.get('save','')
            report = Report.objects.get(pk = report_pk)
            form = ReportEditForm(instance = report)
            groupInvalid = True
            return render_to_response('witness/user_edit_report.html', {'form':form, 'report':report, 'groupInvalid': groupInvalid}, context)

class ReportEditForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_title', 'report_short_description','report_group', 'report_long_description', 'report_public']

def msg3(request):
    if request.method == 'GET':
        results = MessageM.objects.all()
        return render(request, 'witness/messaging3.html', {'results': results})
    else:
        if 'deletebox' in request.POST:
            selected_pk = request.POST.get('deletebox','')
            message = MessageM.objects.get(pk = selected_pk)
            message.delete()
            #results = MessageM.objects.all()
            #print(selected[0])
            #for x in range(0, len(selected)):
            #   todel = MessageM.objects.filter(message=str(selected[x]))
            #   todel.delete()
            #results.delete()
        elif 'decryptbox' in request.POST:
            selected_pk = request.POST.get('decryptbox','')
            message = MessageM.objects.get(pk = selected_pk)
            return render(request, 'witness/decipher.html', {'message': message})
        return HttpResponseRedirect('witness/messaging3.html')

def decipher(request):
    if request.method == 'POST':
        key = request.POST.get('key','')
        key = key.replace('-----BEGIN RSA PRIVATE KEY-----','')
        key = key.replace('----END RSA PRIVATE KEY-----','')
        key = key.replace(' ','\n')
        key = '-----BEGIN RSA PRIVATE KEY-----\n' + key + '\n----END RSA PRIVATE KEY-----'
        #f = open(file_name,'rb')
        #key = RSA.importKey(f.read())
        
        private_key = RSA.importKey(key) #transform back to the private key
        mess_pk = request.POST.get("message",'')
        message = MessageM.objects.get(pk = mess_pk) #get the message we are decrypting
        print(message.message)
        enc_mess = message.message
        enc_mess = base64.b64decode(enc_mess)
        print(enc_mess)
        #hand to the decode method
        dec_mess = decode_string(enc_mess, private_key)
        return render(request, 'witness/decipher.html', {'decoded': True, 'dec_mess':dec_mess})
    else:
        return render(request, 'witness/decipher.html', {'decoded':False})

def keypage(request):
    if request.method == 'GET':
        username = request.user.username
        reporter = Reporter.objects.get(name = username)
        reporter_key = reporter.key1
        pub_key = reporter_key.publickey()
        privkey = reporter_key.exportKey()
        return render(request, 'witness/kpage.html', {'pub_key': pub_key, 'privkey': privkey})
    else:
        return HttpResponseRedirect("/userpage")

def communicate(request):
    data = {}
    username = request.GET.get('username','')
    password = request.GET.get('password', '')
    user = auth.authenticate(username=username, password = password)
    if user is not None:
        data['valid'] = user.is_active
        #get all of the reports this user has access to
        reports = Report.objects.filter(report_owner__exact = user)
        all_reports = Report.objects.all()
        access = []
        for report in all_reports:
            group_name = report.report_group
            #add the report if the user is an a group that can view the report
            if user.groups.filter(name = group_name).exists() and report not in reports:
                access.append(report)
            #add the report if it is public
            if report.report_public and report not in reports and report not in access:
                access.append(report)
        final = list(chain(reports, access)) 
        report_list = []
        for report in final:
            entry =  report.report_title + " (key = " + str(report.pk) + ")"
            report_list.append(entry)
        data['reports'] = report_list
    else:
        data['valid'] = False
    data['username'] = username
    data['password'] = password

    return JsonResponse(data)

def communicate2(request):
    data = {}
    key = request.GET.get('key','')
    report = Report.objects.get(pk = key)

    data['report_title'] = report.report_title
    data['report_short_description'] = report.report_short_description
    data['report_long_description'] = report.report_long_description
    data['report_creation_date'] = str(report.report_creation_date)
    data['report_owner'] = report.report_owner.username
    data['report_public'] = str(report.report_public)
    
    files = report.report_files.split(',')
    file_list = []
    for f in files:
        if f != '':
            if File.objects.filter(pk__exact = int(f)).exists():
                f2 = File.objects.get(pk = int(f))
                file_list.append(str(f2.document.name)+ " (key = " + str(f) + ")")
    data['files'] = file_list

    return JsonResponse(data)

def communicate3(request):
    data = {}
    filekey = request.GET.get('filekey','')
    file = File.objects.get(pk=filekey)
    url = str(file.document.url)
    encrypted = file.document_file_encryption
    data['url'] = url
    data['encrypted'] = encrypted
    return JsonResponse(data)

def secret_string(s, key):
    """Takes in a string and a public key
     encrypts the string with said key
     then returns resulting string"""
    s_e = s.encode()
    enc_data = key.encrypt(s_e, 32)[0] #retrieves the string from the returned tuple
    print ('encrypted: ', enc_data)
    return enc_data

def decode_string(s, key):
    #b = bytes(s, 'utf-8')
    dec_data = key.decrypt(s)
    #print('decoded: ', dec_data.decode())
    #return(dec_data)
    return(dec_data)
