from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    
    
    def __str__(self) -> str:
        return self.title + ' | ' + self.author