# models.py
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/')

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)
    date_created = models.DateField()
