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
from .models import File
from .forms import ReportForm
from .forms import FileForm
from .models import ReportFolder
from .forms import ReportFolderForm
from django.contrib.auth.models import Group
import os
import mimetypes
from securewitness import settings


def createReport(request):
    groupInvalid = False
    invalid_name = False
    if request.method == "POST":
        #Create and save the report
        form = ReportForm(request.POST, request.FILES)
        #if form.is_valid():
        report_title = request.POST.get('report_title', '')
        group_name = request.POST.get('report_group', '')
        groupExists = Group.objects.filter(name = group_name).exists()
        if not groupExists and group_name != '':
            groupInvalid = True
            return render(request, 'reports/createreport.html', {'form':form, 'groupInvalid':groupInvalid})

        report_short_description = request.POST.get('report_short_description', '')
        report_long_description = request.POST.get('report_long_description', '')
        report_location = request.POST.get('report_location', '')
        report_owner = request.user
        report_group = request.POST.get('report_group', '')
        report_public = request.POST.get('report_public', '')
        #report_file = request.FILES['report_file']
        #report_file_encryption = request.POST.get('report_file_encryption', '')
        #report_file = request.POST.get('report_file', '')
        #create the report
        newreport = Report(report_title = report_title, report_location = report_location, report_short_description = report_short_description, 
                report_long_description = report_long_description, report_creation_date = timezone.now(),
                report_owner = report_owner, report_group = report_group, report_public = report_public, report_files = '')
        newreport.save()
        return HttpResponseRedirect("/userpage")
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
            folder_reports1 = folder_reports.split(',')
            folder_reports2 = ''
            for report in folder_reports:
                if Report.objects.filter(report_owner__exact = request.user).filter(report_title__exact = report).exists():
                    report = Report.objects.get(report_owner__exact = request.user).filter(report_title__exact = report)
                    report_pk = report.pk
                    folder_reports2 = folder_reports2 + ',' + str(report_pk)
            newfolder = ReportFolder(folder_title = folder_title, folder_creation_date = timezone.now(),
                    folder_owner = folder_owner, folder_reports = folder_reports2)
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

def addFiles(request):
    context = RequestContext(request)
    if request.method == "GET":
        report_pk = request.GET.get('addfiles', '')
        report = Report.objects.get(pk = report_pk)
        form = FileForm()

        files = report.report_files.split(',')
        file_list = []
        for f in files:
            if f != '':
                if File.objects.filter(pk__exact = int(f)).exists():
                    f2 = File.objects.get(pk = int(f))
                    file_list.append(f2)
        return render_to_response('reports/addfiles.html', {'report': report, 'form':form, 'file_list':file_list}, context)
    if request.method == "POST":
        if request.POST.get('remove','') != '':
            report_pk = request.POST.get('remove', '')
            file_pks = request.POST.getlist('file')
            report = Report.objects.get(pk = report_pk)
            for f in file_pks:
                report.report_files = report.report_files.replace(str(f), '',1)
                report.save()

        elif request.POST.get('add',''):
            report_file = request.FILES['document']
            file_encryption = (request.POST.get('document_file_encryption', '') == 'on')
            newFile = File(document = report_file, document_file_encryption = file_encryption)
            newFile.save()
            file_pk = newFile.pk
            report_pk = request.POST.get('add', '')
            report = Report.objects.get(pk = report_pk)

            report.report_files = report.report_files + str(file_pk) + ','
            report.save()

        files = report.report_files.split(',')
        file_list = []
        for f in files:
            if f != '':
                if File.objects.filter(pk__exact = int(f)).exists():
                    f2 = File.objects.get(pk = int(f))
                    file_list.append(f2)
        form = FileForm()
        return render_to_response('reports/addfiles.html', {'report': report, 'form':form, 'file_list':file_list}, context)



def list(request):
    documents = File.objects.all()
    return render_to_response('reports/download_file.html', {'documents':documents}, context_instance = RequestContext(request))


