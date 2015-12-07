
from securewitness import settings as s  # need it because my database setting are there
dbs = s.DATABASES
from django.conf import settings
settings.configure(DATABASES=dbs) # configure can only be called once
from witness.models import *
from report.models import *


username = input("Enter username: ")
password = input("Enter password: ")
#and user.password == password:

for user in User.objects.all():
	if user.username == username:
		print("Welcome " + user.username + "!")
		for report in Report.objects.all():
			if report.report_owner == user:
				print(str(report))