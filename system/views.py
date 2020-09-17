from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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
        
        user = police.objects.create(policeID = policeID, \
            fullname = fullname, designation = designation, \
                contactNumber = contactNumber, \
                    emailAddress = emailAddress, \
                        username = username, \
                        password = password )

        user.save()

        return redirect ('/login')

    else:
       return render (request, 'signup.html')

def user_login (request):

    if request.method == 'POST':
        username = request.POST ['Username']
        password = request.POST ['Password']

        user = authenticate ( request, username = username, \
            password = password )
  
        if user is not None:
            login (request, user)
            return redirect ('http://127.0.0.1:8000/users/')

        else: 
            return redirect ('http://127.0.0.1:8000/login/')

    else:    
        return render (request, 'login.html')

def users (request):
            
    return render (request, 'Users.html')