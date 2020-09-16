from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import police
#
#class login (forms.ModelForm):
#    class Meta:
##        model = Login 
 #       fields = ['Username', 'Password']

class signup (UserCreationForm):
    class Meta:
        model = police
        fields = [ 'policeID', 'fullname', 'designation', 'contactNumber', 'emailAddress', 'username', 'password']
