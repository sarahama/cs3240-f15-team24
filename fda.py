#import django
#django.setup()
from securewitness import settings as s  # need it because my database setting are there
dbs = s.DATABASES
from django.conf import settings
settings.configure(DATABASES=dbs) # configure can only be called once
#settings.configure()
from witness.models import *
from report.models import *


username = input("Enter username: ")
password = input("Enter password: ")
#and user.password == password:

for user in User.objects.all():
    if user.username == username:
        print("Welcome " + user.username + "!")
        print("Your reports:")
        for report in Report.objects.all():
            if report.report_owner == user:
                print(str(report))

reportToView = input("\nType the name of the report you would like to view:")
file_list = []
for report in Report.objects.all():
    if report.report_title == reportToView:
        print("Title: " + report.report_title)
        print("Owner: " + report.report_owner.username)
        print("Short Description: " + report.report_short_description)
        print("Long Description: " + report.report_long_description)
        print("Files:")
        files = report.report_files.split(',')
        for file in files:
            if file != '':
                if File.objects.filter(pk__exact = int(file)).exists():
                    f2 = File.objects.get(pk = int(file))
                    file_list.append(f2)
        for file in file_list:
            print("\t" + file.document.name)
        print("Date Created: " + str(report.report_creation_date))
        print("Public: " + str(report.report_public))

filename = input("Enter the name of the file you wish to download: ")
for file in file_list:
    if file.document.name == filename:
        if file.document_file_encryption:
            key = "Enter the encyption key to decrypt this file: "
        else:
            print("This file is not encrypted")