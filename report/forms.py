from django import forms
import datetime
from .models import Report, File, ReportFolder

class ReportForm(forms.Form):
    report_title = forms.CharField(label = 'Report Title', max_length = 100)
    report_group = forms.CharField(label = 'Group with access to this report (optional)', max_length = 100)
    report_short_description = forms.CharField(label = 'Short Description', max_length = 100)
    report_long_description = forms.CharField(label = 'Long Description', widget = forms.Textarea)
    #report_file = forms.FileField(label ='Select a file')
    #report_file_encryption = forms.BooleanField(label = 'Is this file encrypted?' ,required = False)
    report_public = forms.BooleanField(required = False)
    


class ReportFolderForm(forms.Form):
	folder_title = forms.CharField(label = 'Folder Name', max_length=200)
	folder_reports = forms.CharField(label = 'Reports in this folder', max_length=1000)

class FileForm(forms.Form):
    document = forms.FileField(label ='Upload a file')
    document_file_encryption = forms.BooleanField(label = 'Is this file encrypted?' ,required = False)



    