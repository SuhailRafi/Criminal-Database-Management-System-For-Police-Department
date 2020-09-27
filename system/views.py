from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
        
        officer = police.objects.create(policeID = policeID, \
            fullname = fullname, designation = designation, \
                contactNumber = contactNumber, \
                    emailAddress = emailAddress, \
                        username = username, \
                        password = password )

        officer.save()

        user = User.objects.create_superuser(username = username, \
            password = password, is_staff = True)
            

        user.save()

        return redirect ('/login')

    else:
       return render (request, 'signup.html')

def user_login (request):

    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']


        user = auth.authenticate ( request, username = username, \
            password = password )
  
        if user is not None:
            auth.login (request, user)
            return redirect ('http://127.0.0.1:8000/users/')

        else: 
            return redirect ('http://127.0.0.1:8000/login/')

    else:    
        return render (request, 'login.html')
     

def users (request):
    users = police.objects.all()
    context = {
        'police': users
    }
    return render (request, 'Users.html', context)