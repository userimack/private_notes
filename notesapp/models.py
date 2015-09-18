from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
	user = models.ForeignKey(User,unique=True)
	title = models.CharField(max_length=30,unique=True)
	note = models.CharField(max_length=1000)

	def __str__(self):
		return self.title
