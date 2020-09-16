from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from .models import police

# Create your views here.

def signup (request):

    if request.method == 'POST':
        policeID = request.POST ['policeID']
        fullname = request.POST ['FullName']
        designation = request.POST ['Designation']
        contactNumber = request.POST ['ContactNumber']
        emailAddress = request.POST ['EmailAddress']
        username = request.POST ['Username']
        password = request.POST ['Password']
        
        x = police.objects.create(policeID = policeID, \
            fullname = fullname, designation = designation, \
                contactNumber = contactNumber, \
                    emailAddress = emailAddress, \
                        username = username, \
                        password = password )

        x.save()

        return redirect ('/login')

    else:
       return render (request, 'signup.html')

def login (request):

    if request.method == 'POST':
        username = request.POST ['Username']
        password = request.POST ['Password']

        x = auth.authenticate ( username = username, \
            password = password )

        if x is None:

            redirect ('/')
        else: 

            redirect ('/Users')

    else:    
        return render (request, 'login.html')
      


def users (request):
            
    return render (request, 'Users.html')