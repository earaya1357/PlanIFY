from django.forms import ModelForm
from django import forms
from .models import UserAccount, Event, EventParticipant, EventWorkOut, EventVendor, Vendor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_host_user', 'event_host_affiliate', 'event_name', 'event_date', 'event_size', 'event_location', 'event_address', 'event_phone_number', 'event_description']


class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class EventParticipantForm(ModelForm):
    class Meta:
        model = EventParticipant
        fields = ['event_id_number', 'first_name_of_athlete', 'last_name_of_athlete', 'email_of_athlete']


class EventName(forms.Form):
    name = forms.CharField(max_length=50)

