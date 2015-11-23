from django import forms
import datetime
from .models import Report, File, ReportFolder

class ReportForm(forms.Form):
    report_title = forms.CharField(label = 'Report Title', max_length = 100)
    report_short_description = forms.CharField(label = 'Short Description', max_length = 100)
    report_long_description = forms.CharField(label = 'Long Description', widget = forms.Textarea)
    report_public = forms.BooleanField(required = False)
    report_file = forms.FileField(label ='Select a file')
    report_file_encryption = forms.BooleanField(label = 'Is this file encrypted?' ,required = False)
