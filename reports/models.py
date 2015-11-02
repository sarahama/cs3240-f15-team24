
from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length = 60)
