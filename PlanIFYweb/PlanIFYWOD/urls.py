from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('eventdesign/<str:eventname>', views.eventdesign, name='EventDesign'),
    path('register', views.register, name='Register'),
    path('sign-in', views.usersignin, name='SignIn'),
    path('sign-out', views.usersignout, name='SignOut'),
    path('complete-registration/<str:username>', views.completeregistration, name='CompleteRegistration'),
    path('your-events/<int:id>', views.hostedevents, name='HostedEvent'),
    path('event/prepare/<str:event>', views.prepareevent, name='PrepareEvent'),
    path('PlanIFY', views.homepage, name='Landing'),
    path('profile/<str:user>', views.userprofile, name='Profile'),
    path('PlanIFY/find-event', views.eventserach, name='EventSearch'),
   # path('find-event/event/<str:event>', views.generalevent, name='GeneralEvent'),
]