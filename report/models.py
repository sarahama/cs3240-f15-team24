import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission, Group
#from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location='/media/files')

# Create your models here.
class ReportFolder(models.Model):
    folder_title = models.CharField(max_length=200)
    folder_creation_date = models.DateTimeField('date published')
    folder_owner = models.ForeignKey('auth.User')
    def __str__(self):
        return self.folder_title

class Report(models.Model):
    report_title = models.CharField(max_length=64)
    report_short_description = models.TextField(max_length = 500)
    report_long_description = models.TextField(blank = True)
    report_creation_date = models.DateTimeField('date published')
    report_owner = models.ForeignKey('auth.User')
    #report_files = models.FileField(upload_to = 'files')
    report_public = models.BooleanField(default = False)
    #report_folder = models.ForeignKey(ReportFolder)
    def __str__(self):
        return self.report_title

class File(models.Model):
    report = models.ForeignKey(Report)
    document = models.FileField(upload_to = 'documents/%Y/%m/%d', default= 'unknown')
    def __str__(self):
        return self.file_name
