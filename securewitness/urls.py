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
#from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^adminhome/', 'witness.views.admin_home', name = 'adminhome'),
    url(r'^adminuser/', 'witness.views.admin_users', name = 'adminuser'),
    url(r'^adminreports/', 'witness.views.admin_reports', name = 'adminreports'),
    url(r'^adminviewreport/', 'witness.views.admin_view_report', name = 'adminviewreport'),
    url(r'^edituser/', 'witness.views.admin_edit_user', name = 'edituser'),
    url(r'^accesserror/', 'witness.views.access_error', name = 'errorpage'),
    url(r'^createreport/', 'report.views.createReport', name='createreport'),
    url(r'^creategroup/', 'witness.views.creategroup', name = 'creategroup'),
    url(r'^addgroup/', 'witness.views.addgroup', name = 'addgroup'),
    url(r'^grouphome/', 'witness.views.grouphome', name = 'grouphome'),
    url(r'^userpage/', 'witness.views.userpage', name = 'userpage'),
    url(r'^userreports', 'witness.views.user_reports', name = 'userreports'),
    url(r'^userviewreport', 'witness.views.user_view_report', name = 'userviewreport'),
    url(r'^login/', 'witness.views.login', name = 'login'),
    url(r'^logout/', 'witness.views.logout', name = 'logout'),
    url(r'^super/', 'witness.views.super', name = 'super'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'witness.views.register', name = 'register'),
    url(r'^registration_success/', 'witness.views.registration_success', name = 'success'),
    url(r'^messaging/', 'witness.views.get_Message', name = 'messaging'),
    url(r'^messaging2/', 'witness.views.get_Message', name = 'messaging2'),
    url(r'^messaging3/', 'witness.views.msg3', name = 'messaging3'),
    url(r'^$', 'witness.views.home', name='home'),
]
