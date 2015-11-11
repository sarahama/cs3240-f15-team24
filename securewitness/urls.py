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
	url(r'^userpage/', 'witness.views.userpage', name = 'userpage'),
    url(r'^login/', 'witness.views.login', name = 'login'),
    url(r'^logout/', 'witness.views.logout', name = 'logout'),
    url(r'^super/', 'witness.views.super', name = 'super'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'witness.views.register', name = 'register'),
    url(r'^registration_success/', 'witness.views.registration_success', name = 'success'),
    url(r'^$', 'witness.views.home', name='home'),
]
