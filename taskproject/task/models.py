from enum import auto
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title