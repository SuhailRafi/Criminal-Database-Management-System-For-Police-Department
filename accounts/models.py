from django.db import models

# Create your models here.

class criminal (models.Model): 
    name = models.CharField (max_length=200)
    age = models.IntegerField ()
    gender = models.CharField (max_length=6)
    height = models.CharField (max_length=7)
    nationality = models.EmailField(max_length=20)
    nationalID = models.CharField (max_length=20)
    criminalID = models.CharField (max_length=20)
    presentPrison = models.CharField (max_length=20) 
    previousCrimeRecord = models.CharField (max_length=20)
    criminalImage = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    fringerPrint = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    footPrint = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    
    def __str__(self):
        return self.name, self.age, self.gender, self.height, \
            self.nationality, self.criminalID, self.presentPrison, \
                self.previousCrimeRecord, self.criminalImage, \
                    self.fingerPrint, self.footprint
        

class crime (models.Model): 
    crimeType = models.CharField (max_length=20)
    crimeDescription = models.TextField (max_length=500)
    dateOfCrime = models.DateField () #recheck
    victims = models.TextField (max_length=200)
    FIRNumber = models.CharField (max_length=20)
    officerOnDuty = models.CharField (max_length=20)
    fieldOfInterest = models.CharField (max_length=20)
    
    def __str__(self):
        return self.crimeType, self.crimeDescription, self.dateOfCrime,\
             self.victims, self.FIRNumber, self.officerOnDuty, \
                 self.fieldOfInterest 
