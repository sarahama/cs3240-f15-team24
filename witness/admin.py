from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MessageM
from .models import Reporter

# Register your models here.

class ReporterInline(admin.StackedInline):
    model = Reporter
    list_display = ('username')

#class UserAdmin(UserAdmin):
#    inlines = (ReporterInline, )

#class ReporterAdmin(ReporterAdmin):
#    model = Reporter
#    inlines = [ChoiceInLine]
#    list_display = ('username')

class MessageAdmin(admin.ModelAdmin):
	fields = ('reader', 'message')

admin.site.register(MessageM, MessageAdmin)
admin.site.unregister(User)
admin.site.register(Reporter)
admin.site.register(User, UserAdmin)

