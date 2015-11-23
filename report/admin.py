from django.contrib import admin

from .models import Report, ReportFolder, File
from witness.models import Reporter

class ReportAdmin(admin.ModelAdmin):
    fields = ('report_title','report_short_description','report_long_description', 'report_creation_date', 'report_owner','report_public','report_file','report_file_encryption')

class FolderAdmin(admin.ModelAdmin):
    fields = ('folder_title', 'report_owner')



admin.site.register(Report, ReportAdmin)
admin.site.register(ReportFolder, FolderAdmin)
