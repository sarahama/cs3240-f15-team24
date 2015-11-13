from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reporter(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 50, default= 'nameless')