from django.contrib import admin

# Register your models here.
from .models import Report, ReportFolder
from witness.models import Reporter

class ReportAdmin(admin.ModelAdmin):
     list_distplay = ('report_title','report_short_description','report_long_description', 'report_creation_date', 'report_owner','report_files','report_public')

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportFolder)