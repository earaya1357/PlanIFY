from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboarddata, name='Dashboard'),
    path('create-event', views.createevent, name='CreateEvent'),
    path('user-account', views.useraccount, name='UserAccount'),
    path('user', views.user, name='User'),
    path('new-user', views.createnewuser, name='NewUser'),
    path('new-user-profile', views.createuserprofile, name='NewUserProfile'),
    path('test', views.getmodeldetails, name='Test'),
    path('events-dashboard-host', views.vieweventshost, name='ViewEventsHost'),
    path('events-dashboard-host-edit', views.editeventshost, name='EditEventsHost'),
    path('events-dashboard-athlete', views.vieweventsathlete, name='ViewEventsAthlete'),
]   