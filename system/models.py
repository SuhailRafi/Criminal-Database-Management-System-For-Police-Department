from django.db import models

# Create your models here.
class login (models.Model):
    username = models.CharField (max_length=50)
    password = models.IntegerField ()
   
    def __str__(self):
        return self.username, self.password

class police (models.Model): 
    policeID = models.CharField (max_length=10)
    fullname = models.CharField (max_length=200)
    designation = models.CharField (max_length=50)
    contactNumber = models.CharField (max_length=11)
    emailAddress = models.EmailField(max_length=200)
    username = models.CharField (max_length=50)
    role = models.CharField (max_length=10)
    password = models.CharField (max_length=50)
    confirmPassword = models.CharField (max_length=50)
    
    def __str__(self):
        return self.fullname, self.designation, \
            self.policeID, self.contactNumber, \
                self.emailAddress, self.username, \
                    self.password, self.confirmPassword

