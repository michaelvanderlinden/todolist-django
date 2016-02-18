from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Task(models.Model):
    taskname = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    #collaborators = models.something(Users, max = 3)