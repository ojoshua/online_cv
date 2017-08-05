from django.db import models

class DemoCategory(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __str__(self):
		return self.name

class Demo(models.Model):
	category = models.ForeignKey(DemoCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	of_what = models.TextField()
	brief_description = models.TextField()
	long_description = models.TextField()
	url = models.URLField()
	url.blank = True
	def __str__(self):
		return self.name

class Message(models.Model):
	sender = models.CharField(max_length=100)
	contact_info = models.CharField(max_length=100)
	content = models.TextField()
	def __str__(self):
		return self.sender+' '+self.contact_info