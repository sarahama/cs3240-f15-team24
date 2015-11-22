from django import forms
from django.contrib.auth.models import User
from .models import MessageM

class CreateGroupForm(forms.Form):
	name = forms.CharField(label="Group Name")


class MessageF(forms.ModelForm):
	class Meta:
		model = MessageM
		fields = "__all__"

class GroupDisplay(forms.Form):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(GroupDisplay, self).__init__(*args, **kwargs)

	def displayGroups(self):
		groupList = []
		for group in self.request.user.groups():
			groupList.append(group)
		groups = forms.MultipleChoiceField(choices = groupList)