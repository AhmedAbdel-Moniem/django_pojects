from django.db import models

# Create your models here.
class AppOne(models.Model):
	item_name  = models.TextField()
	price      = models.TextField()
	description= models.TextField()
	summary    = models.TextField()