from django.db import models

# Create your models here.
class AppOne(models.Model):
	item_name  = models.CharField(max_length=120)  #max_length = required
	price      = models.DecimalField(decimal_places=2, max_digits=10000)
	description= models.TextField(blank=False, null=True)
	summary    = models.TextField(blank=False)
	feature    = models.BooleanField()
	feature2   = models.BooleanField(default=True)