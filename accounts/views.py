from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registerCrime (request):
    return render (request, 'Criminal Registration.html')
def criminal (request):
    return render (request, 'Criminals.html')           
def crime (request):
    return render (request, 'Crime.html')