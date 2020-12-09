from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=55)
    hint = models.CharField(max_length=100)
    description = models.TextField()
    summary = models.TextField()
    price = models.DecimalField(max_digits=2, decimal_places=True)

    def __repr(self):
        return str(self.title + ' | ' + self.hint)

    def get_absolute_url(self):
        return reverse('myapp:list_items', kwargs={'id': self.id})
