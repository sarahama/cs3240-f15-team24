"""securewitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

    url(r'^login/', 'witness.views.login', name ='login'),
    url(r'^register/', 'witness.views.register', name = 'register'),

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from securewitness import settings
import os
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^adminhome/', 'witness.views.admin_home', name = 'adminhome'),
    url(r'^adminuser/', 'witness.views.admin_users', name = 'adminuser'),
    url(r'^adminreports/', 'witness.views.admin_reports', name = 'adminreports'),
    url(r'^adminviewreport/', 'witness.views.admin_view_report', name = 'adminviewreport'),
    url(r'^edituser/', 'witness.views.admin_edit_user', name = 'edituser'),
    url(r'^editreport/', 'witness.views.user_edit_report', name = 'editreport'),
    url(r'^accesserror/', 'witness.views.access_error', name = 'errorpage'),
    url(r'^createreport/', 'report.views.createReport', name='createreport'),
    url(r'^addfiles/', 'report.views.addFiles', name='addfiles'),
    url(r'^list', 'report.views.list', name = 'list'),
    url(r'^creategroup/', 'witness.views.creategroup', name = 'creategroup'),
    url(r'^createfolder/', 'report.views.createFolder', name = 'createfolder'),
    #url(r'^addgroup/', 'witness.views.addgroup', name = 'addgroup'),
    url(r'^grouphome/', 'witness.views.grouphome', name = 'grouphome'),
    url(r'^viewgroup/', 'witness.views.user_view_group', name = 'viewgroup'),
    url(r'^userpage/', 'witness.views.userpage', name = 'userpage'),
    url(r'^userreports', 'witness.views.user_reports', name = 'userreports'),
    url(r'^userviewreport', 'witness.views.user_view_report', name = 'userviewreport'),
    url(r'^deletedreport', 'witness.views.deleted_report', name = 'deletedreport'),
    url(r'^userfolders', 'witness.views.user_folders', name = 'userfolders'),
    url(r'^userviewfolders', 'witness.views.user_view_folders', name = 'userviewfolders'),
    url(r'^login/', 'witness.views.login', name = 'login'),
    url(r'^logout/', 'witness.views.logout', name = 'logout'),
    url(r'^super/', 'witness.views.super', name = 'super'),
    url(r'^register/', 'witness.views.register', name = 'register'),
    url(r'^registration_success/', 'witness.views.registration_success', name = 'success'),
    url(r'^messaging/', 'witness.views.get_Message', name = 'messaging'),
    url(r'^messaging2/', 'witness.views.get_Message', name = 'messaging2'),
    url(r'^messaging3/', 'witness.views.msg3', name = 'messaging3'),
    url(r'^$', 'witness.views.login', name = 'login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

