from django.db import models
from django.utils import timezone

# Create your models here.

class Contact (models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    phone = models.CharField (max_length = 255)
    email = models.EmailField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    trashed = models.BooleanField(default = False)

    def __str__(self):
        return self.firstname

class ActivityLog(models.Model):
    activity = models.CharField(max_length = 255)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.activity
