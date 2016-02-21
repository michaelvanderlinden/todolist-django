from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    
class Task(models.Model):
    ownerid = models.ForeignKey(UserProfile, related_name="owned_tasks")
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(UserProfile, related_name="tasks")