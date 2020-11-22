from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=55)    
    description = models.TextField()
    summary     = models.TextField()

    def __str__(self):
        return self.title 
