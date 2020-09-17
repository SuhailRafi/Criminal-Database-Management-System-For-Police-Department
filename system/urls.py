from django.urls import path
from system import views

urlpatterns = [
    path ('login/', views.user_login, name='Login'),
    path ('users/', views.users, name='Users'),
    path ('signup/', views.signup, name='Sign up'),
]
