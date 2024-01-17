from rest_framework import serializers
from django.contrib.auth.models import User
from django.apps import apps

Event = apps.get_model('PlanIFYWOD', 'Event')
UserAccount = apps.get_model('PlanIFYWOD', 'UserAccount')
EventParticipant = apps.get_model('PlanIFYWOD', 'EventParticipant')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = '__all__'
