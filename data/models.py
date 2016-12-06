from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    branches = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('data:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' (' + self.code + ')'


class Book(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    subject = models.CharField(max_length=100)
    image = models.FileField()
    #subcode = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('data:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author + '-' + self.title


