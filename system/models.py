from django.db import models
from django.conf import settings
# Create your models here.

class police (models.Model): 
    policeID = models.CharField( settings.AUTH_USER_MODEL, max_length=200,)
    fullname = models.CharField (max_length=200)
    designation = models.CharField (max_length=50)
    contactNumber = models.CharField (max_length=11)
    emailAddress = models.EmailField(max_length=200)
    username = models.CharField (max_length=50)
    role = models.CharField (max_length=10)
    password = models.CharField (max_length=50)
    
    def __str__(self):
        return self.username
