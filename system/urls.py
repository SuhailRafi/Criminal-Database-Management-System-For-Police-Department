from django.urls import path
from system import views

urlpatterns = [
    path ('login/', views.login, name='login'), #redirects to views.py and searches for home function for functionality
    path ('registration/', views.registration, name='registration'),
    path ('data/', views.data, name='data'),
]
