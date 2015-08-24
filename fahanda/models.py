from django.db import models

class Index(models.Model):
	image = models.CharField(max_length=100)

class News(models.Model):
	news = models.CharField(max_length=1000)
	image =

class Products(models.Model):
	image =
	description = models.CharField(max_length=200)

class Projects(models.Model):
	image =
	description = models.CharField(max_length=1000)

class About(models.Model):
	image =
	history = 

class Contact(models.Model):
	address =
	email =
	location =
	telephone =
