from django import forms
from django.contrib.auth.models import User
from .models import MessageM

class GroupForm(forms.Form):
	userList = User.objects.all()
	tup_list = []
	for user in userList:
		tup = (user.id, user.username)
		tup_list.append(tup)
	name = forms.CharField(label="Group Name")
	other_users = forms.MultipleChoiceField(choices = tup_list)


class MessageF(forms.ModelForm):
	class Meta:
		model = MessageM
		fields = "__all__"
