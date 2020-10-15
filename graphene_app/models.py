from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date


# Tasks Models
class task(models.Model):
    user = models.CharField(blank=False, max_length=100)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
