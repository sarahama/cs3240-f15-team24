from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Reporter
# Register your models here.

class ReporterInline(admin.StackedInline):
    model = Reporter

class UserAdmin(UserAdmin):
    inlines = (ReporterInline, )

admin.site.unregister(User)
admin.site.register(Reporter)
#admin.site.register(User, UserAdmin)

