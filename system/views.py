from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login (request):
    return render (request, 'login.html')
def registration (request):
    return render (request, 'Criminal Registration.html')
def data (request):
    return render (request, 'Criminals.html')   
