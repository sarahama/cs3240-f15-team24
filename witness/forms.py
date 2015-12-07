from django import forms
from django.contrib.auth.models import User, Group
from .models import MessageM

class CreateGroupForm(forms.Form):
	name = forms.CharField(label="Group Name")


class MessageF(forms.Form):
	reader = forms.CharField(label = 'Send to', max_length = 100)
	message = forms.CharField(label = 'Message', widget = forms.Textarea)

class AddGroup(forms.Form):
	name = forms.CharField(label="Group Name")
	member = forms.CharField(label="User to add")

class AddMember(forms.Form):
	member = forms.CharField(label="User to add")