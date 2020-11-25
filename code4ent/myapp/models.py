from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=55)
    hint = models.CharField(max_length=100)
    description = models.TextField()
    summary = models.TextField()
    price = models.DecimalField(max_digits=2, decimal_places=True)

    def __str__(self):
        return (self.title + ' | ' + self.hint)
