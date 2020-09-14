from django.urls import path
from system import views

urlpatterns = [
    path ('signin/', views.signin, name='Sign In'),
    path ('users/', views.users, name='Users'),
]
