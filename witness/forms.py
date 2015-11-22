from django import forms
from django.contrib.auth.models import User

class GroupForm(forms.Form):
	userList = User.objects.all()
	tup_list = []
	for user in userList:
		tup = (user.id, user.username)
		tup_list.append(tup)
	name = forms.CharField(label="Group Name")
	other_users = forms.MultipleChoiceField(choices = tup_list)


