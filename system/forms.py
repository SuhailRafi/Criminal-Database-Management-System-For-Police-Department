from django import forms 
from .models import login
from .models import police

class login (forms.ModelForm):
    class Meta:
        model = Login 
        fields = ['Username', 'Password']

class police (forms.ModelForm):
    class Meta:
        model = Police
        fields = [ 'Police ID', 'Full Name', 'Designation', 'Contact Number', 'Email Address', 'Username', 'Role', 'Password', 'Confrim Password']

