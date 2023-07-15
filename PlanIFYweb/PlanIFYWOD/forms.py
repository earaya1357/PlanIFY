from django.forms import ModelForm
from django import forms
from .models import UserAccount, Event, EventParticipant, EventWorkOut, EventVendor, Vendor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateIn(forms.DateInput):
    input_type = 'date'


class TimeIn(forms.TimeInput):
    input_type = 'time'


class EventWorkoutForm(ModelForm):
    class Meta:
        model = EventWorkOut
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_date': DateIn(),
            'event_start_time' : TimeIn(),
            'event_date_created': DateIn(),
            'event_registration_date_open': DateIn(),
            'event_registration_date_close': DateIn(),
        }

class FullEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_date': DateIn(),
            'event_start_time' : TimeIn(),
            'event_date_created': DateIn(),
            'event_registration_date_open': DateIn(),
            'event_registration_date_close': DateIn(),
        }


class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'
        widgets = {
            'birthday_user' : DateIn(),
            'email_user' : forms.EmailInput()
        }



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class EventParticipantForm(ModelForm):
    class Meta:
        model = EventParticipant
        fields = ['event_name','first_name_of_participant', 'last_name_of_participant', 'birthday_of_participant', 'gender_of_participant', 'email_of_participant', 'address_of_participant','city_of_participant', 'zip_code_of_participant', 'role', 'team']


class EventName(forms.Form):
    name = forms.CharField(max_length=50)


class AffiliateSearch(forms.Form):
    affiliate_name = forms.CharField(max_length=50)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'
        widgets = {
            'birthday_user' : DateIn(),
            'email_user' : forms.EmailInput()
        }
