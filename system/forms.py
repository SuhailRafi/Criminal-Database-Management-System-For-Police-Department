from django import forms 
from .models import login
from .models import registration

class login (forms.ModelForm):
    class Meta:
        model = Login 
        fields = ['Username', 'Password']

class registration (forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['Full Name', 'Designation', 'Police ID', 'Contact Number', 'Email Address', 'Username', 'Password', 'Confrim Password']

