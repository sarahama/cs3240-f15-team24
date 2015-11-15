from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import ReportForm

from .models import Report

def createReport(request):
    
    if request.method == "POST":
        #Create and save the report
        report_title = request.POST.get('report_title', '')
        report_short_description = request.POST.get('report_short_description', '')
        report_long_description = request.POST.get('report_long_description', '')
        report_creation_date = request.POST.get('report_creation_date', '')
        report_owner = request.user
        report_public = request.POST.get('report_public', '')
        #create the report
        newreport = Report(report_title = report_title, report_short_description = report_short_description, report_long_description = report_long_description, report_creation_date = report_creation_date, report_owner = report_owner, report_public = report_public)
        newreport.save()
    else:
        #display the create report page using the create report form
        form = ReportForm()
        return render(request, 'reports/createreport.html', {'form':form})

