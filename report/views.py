from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

#import os
#from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
from .models import Report
from .forms import ReportForm
from .models import ReportFolder
from .forms import ReportFolderForm
from django.contrib.auth.models import Group


def createReport(request):
    groupInvalid = False
    invalid_name = False
    if request.method == "POST":
        #Create and save the report
        form = ReportForm(request.POST, request.FILES)
        #if form.is_valid():
        report_title = request.POST.get('report_title', '')
        if not Report.objects.filter(report_title = report_title).exists():
            group_name = request.POST.get('report_group', '')
            groupExists = Group.objects.filter(name = group_name).exists()
            if not groupExists and group_name != '':
                groupInvalid = True
                return render(request, 'reports/createreport.html', {'form':form, 'groupInvalid':groupInvalid})

            report_short_description = request.POST.get('report_short_description', '')
            report_long_description = request.POST.get('report_long_description', '')
            report_owner = request.user
            report_group = request.POST.get('report_group', '')
            report_public = request.POST.get('report_public', '')
            report_file = request.FILES['report_file']
            report_file_encryption = request.POST.get('report_file_encryption', '')
            #report_file = request.POST.get('report_file', '')
            #create the report
            newreport = Report(report_title = report_title, report_short_description = report_short_description, 
                    report_long_description = report_long_description, report_creation_date = timezone.now(),
                    report_owner = report_owner, report_group = report_group, report_public = report_public, report_file = report_file, report_file_encryption = report_file_encryption)
            newreport.save()
            return HttpResponseRedirect("/userpage")
        else:
            form = ReportForm()
            return render(request, 'reports/createreport.html', {'form':form, 'invalid_name':True})
    else:
        #display the create report page using the create report form
        form = ReportForm()
        return render(request, 'reports/createreport.html', {'form':form})

def createFolder(request):
    invalid_name = False
    if request.method == "POST":
        #Create and save the report
        form = ReportFolderForm(request.POST)
        #if form.is_valid():
        folder_title = request.POST.get('folder_title', '')
        if not ReportFolder.objects.filter(folder_title = folder_title).filter(folder_owner = request.user).exists():
            folder_owner = request.user
            folder_reports = request.POST.get('folder_reports', '')
            newfolder = ReportFolder(folder_title = folder_title, folder_creation_date = timezone.now(),
                    folder_owner = folder_owner, folder_reports = folder_reports)
            newfolder.save()
            return HttpResponseRedirect("/userpage")
        else:
            form = ReportFolderForm()
            invalid_name = True
            return render(request, 'reports/createfolder.html', {'form':form, 'invalid_name':invalid_name})
    else:
        #display the create folder page using the create report form
        form = ReportFolderForm()
        return render(request, 'reports/createfolder.html', {'form':form})

