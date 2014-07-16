from django.db import models
from django.contrib.auth.models import User
	

class profile(models.Model):	
	def url(self, filename):
		routetofile = "MultimediaData/Users/%s/%s"%(self.nickname.username, filename)
		return routetofile 	
	nickname = models.OneToOneField(User, related_name="profile", unique=True)
	avatar = models.ImageField(upload_to=url)
	CHOICES=[('Python','Python'),('Linux','GNU/Linux')]
	selection =  models.CharField(choices=CHOICES,max_length=12)

	def __unicode__(self):
		return self.nickname.username
