from django.db import models
from django.contrib.auth.models import User, Group
from django import forms
# Create your models here.

class Reporter(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 50, default= 'nameless')
    def __str__(self):
        return self.name

class MessageM(models.Model):
	author = models.CharField(max_length=40)
	message = models.TextField()
	def __str__(self):
		return self.author
