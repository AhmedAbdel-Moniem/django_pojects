from django.db import models

# Create your models here.

class Train(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.TextField(default="")
    name = models.TextField(max_length = 40,default="")
    stud_class = models.TextField(max_length=30,default="")
    department = models.TextField(max_length=30,default="")

 