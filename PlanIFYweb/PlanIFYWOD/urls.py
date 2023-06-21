from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('new-event', views.createnewevent, name='NewEvent'),
    path('register', views.register, name='Register'),
    path('sign-in', views.usersignin, name='SignIn'),
    path('sign-out', views.usersignout, name='SignOut'),
    path('complete-registration/<str:username>', views.completeregistration, name='CompleteRegistration'),
]