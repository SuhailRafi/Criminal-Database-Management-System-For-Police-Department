from django.db import models

# Create your models here.
      
class criminal (models.Model): 
    nationalID = models.CharField (max_length=20)
    name = models.CharField (max_length=200)
    age = models.IntegerField ()
    gender = models.CharField (max_length=6)
    height = models.CharField (max_length=7)
    nationality = models.EmailField(max_length=20)
    criminalImage = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    fringerPrint = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    footPrint = models.ImageField(upload_to=None, height_field=None, \
        width_field=None, max_length=100)
    
    def __str__(self):
        return self.nationalID, self.name, self.age, self.gender, \
            self.height, self.nationality, self.criminalImage, \
                    self.fingerPrint, self.footprint
        
class crime (models.Model): 
    FIRNumber = models.CharField (max_length=20)
    crimeType = models.CharField (max_length=20)
    crimeDescription = models.TextField (max_length=500)
    dateOfCrime = models.DateField () 
    victims = models.TextField (max_length=200)
    officerOnDuty = models.CharField (max_length=20)
    fieldOfConcern = models.CharField (max_length=20)
    
    def __str__(self):
        return self.FIRNumber, self.crimeType, self.crimeDescription, \
            self.dateOfCrime, self.victims, self.officerOnDuty, \
                 self.fieldOfConcern

class crime (models.Model):

    def __str__(self):
        return 