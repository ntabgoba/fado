import datetime
from django.db import models

PRODUCT_CHOICES = (
	('A', 'Aclaric'),
	('C', 'Canvas'),
)

class Index(models.Model):
	name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name 

class New(models.Model):
	title = models.CharField(max_length=200)
	news = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title
	

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	material = models.CharField(max_length=1, choices=PRODUCT_CHOICES)
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	def __unicode__(self):
		return self.name
	
	
class About(models.Model):
	about = models.CharField(max_length=200)
	history = models.TextField(blank=True)
	def __unicode__(self):
		return self.about

class Contact(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	email = models.EmailField()
	location = models.CharField(max_length=200)
	telephone = models.IntegerField()
	def __unicode__(self):
		return self.name



