from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboarddata, name='Dashboard'),
    path('create-event', views.createevent, name='CreateEvent'),
    path('user-account', views.useraccount, name='UserAccount'),
    path('user', views.user, name='User'),
]   