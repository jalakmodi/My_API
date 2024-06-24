from django.db import models
# Create your models here.

class Msg(models.Model):
	title=models.CharField(max_length=100,blank=True)
	content=models.CharField(max_length=100,blank=True)
	isbn=models.CharField(max_length=100,blank=True)
	sender=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.title