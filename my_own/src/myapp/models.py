from django.db import models

# Create your models here.
class my_model_app(models.Model):
	""" our model class """
	title       = models.CharField(max_length=100)
	description = models.TextField() 
	price       = models.DecimalField(max_digits=5, decimal_places=2)