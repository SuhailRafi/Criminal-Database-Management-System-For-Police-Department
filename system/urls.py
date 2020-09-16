from django.urls import path
from system import views

urlpatterns = [
    path ('login/', views.login, name='Log in'),
    path ('users/', views.users, name='Users'),
    path ('signup/', views.signup, name='Sign up'),
]
