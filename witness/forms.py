from django import forms
from django.contrib.auth.models import User, Group
from .models import MessageM

class CreateGroupForm(forms.Form):
	name = forms.CharField(label="Group Name")


class MessageF(forms.ModelForm):
	class Meta:
		model = MessageM
		fields = "__all__"

class AddGroup(forms.Form):
	name = forms.CharField(label="Group Name")
	member = forms.CharField(label="User to add")