import datetime
from django.db import models
from django.utils import timezone
from witness.models import Reporter


# Create your models here.

class Report(models.Model):
    report_title = models.CharField(max_length=64)
    report_short_description = models.TextField(max_length = 500)
    report_long_descpription = models.TextField(blank = True)
    report_creation_date = models.DateTimeField('date published')
    report_owner = models.ForeignKey(Reporter)
    report_files = models.FileField(upload_to = 'report', blank = true)
    report_public = models.BooleanField(default = False)
    def __str__(self):
        return self.title

class ReportFolder(models.Model):
    folder_title = models.CharField(max_length=200)
    folder_creation_date = models.DateTimeField('date published')
    folder_owner = models.ForeignKey(Reporter)
    def __str__(self):
        return self.title

class File(models.Model):
    report = models.ForeignKey(Report)
    file_name = models.CharField(max_length = 30)
    def __str__(self):
        return self.file_name
class Accessibility(models.Model):
    return
