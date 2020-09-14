from django.urls import path
from accounts import views

urlpatterns = [
    path ('registration/', views.registerCrime, name='Crime Registration'),
    path ('criminal/', views.criminal, name='Criminal'),
    path ('crime/', views.crime, name='Crime'),
]
