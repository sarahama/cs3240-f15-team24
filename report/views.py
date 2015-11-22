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
from .forms import ReportForm
from django.utils import timezone
from django.db import models

from .models import Report

def createReport(request):
    
    if request.method == "POST":
        #Create and save the report
        report_title = request.POST.get('report_title', '')
        report_short_description = request.POST.get('report_short_description', '')
        report_long_description = request.POST.get('report_long_description', '')
        report_owner = request.user
        report_public = request.POST.get('report_public', '')
        #report_file = request.POST.get('report_file', '')
        #create the report
        newreport = Report(report_title = report_title, report_short_description = report_short_description, 
                    report_long_description = report_long_description, report_creation_date = timezone.now(),
                    report_owner = report_owner, report_public = report_public)
        newreport.save()
        return HttpResponseRedirect("/userpage")
    else:
        #display the create report page using the create report form
        form = ReportForm()
        return render(request, 'reports/createreport.html', {'form':form})

class ReportList(ListView):
    model = Report
