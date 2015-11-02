from django.db import models

# Create your models here.


#Users have a username, password, and 2 boolean values, admin and disabled
#to describe their status

class User(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	admin = models.IntegerField(default = 0)
	disabled = models.IntegerField(default = 0)
	def __str__(self):
                return self.username

#An additional table to contain reports?	
