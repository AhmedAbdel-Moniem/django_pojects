from django.db import models


class My_API_Model(models.Model):
    api_name = models.CharField(max_length=55)
    api_details = models.CharField(max_length=55)

    def __str__(self):
        return self.api_name + ' | ' + self.api_details