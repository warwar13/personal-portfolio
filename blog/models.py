from django.db import models
import datetime
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title