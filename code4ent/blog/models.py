from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' | ' + self.content

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'id': self.id})