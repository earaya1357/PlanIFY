from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework.authtoken.models import Token
from .serializers import EventSerializer, UserAccountSerializer, UserSerializer, EventParticipantSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.apps import apps

Event = apps.get_model('PlanIFYWOD', 'Event')
UserAccount = apps.get_model('PlanIFYWOD', 'UserAccount')
EventParticipant = apps.get_model('PlanIFYWOD', 'EventParticipant')

@api_view(['POST'])
@csrf_protect
def createnewuser(request):
    data = request.data

    username = data['username']
    password = data['password']
    re_password = data['re_password']
    email = data['email']

    if password == re_password:
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'})
        else:
            if len(password) < 6:
                return Response({'error': 'Password must be at least 6 characters'})
            else:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'This email is already in use'})
                else:
                    serializer = UserSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        print(serializer.validated_data)
                        return Response({'data': serializer.validated_data})
                    return Response({'error': 'Failed to create user'})
    else:
        return Response({'error': 'Passwords do not match'})


@api_view(['POST'])
@csrf_protect
def createuserprofile(request):
    data = request.data
    if UserAccount.objects.filter(username=data['username']).exists():
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.validated_data})
        else:
            return Response({'error': 'Fields missing'})
    else:
        return Response({'error': 'Unable to find the user'})



@api_view(['GET'])
def dashboarddata(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@csrf_protect
def createevent(request):
    event = EventSerializer(data=request.data)

    return Response(event.data.keys())

@api_view(['GET'])
@csrf_protect
def useraccount(request):
    param = request.query_params
    user = get_object_or_404(UserAccount, username=param['id'])
    if not user:
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserAccountSerializer(instance=user)

    return Response({'user': serializer.data})


@api_view(['GET'])
@csrf_protect
def user(request):
    param = request.query_params
    user = get_object_or_404(User, username=param['username'])
    if not user.check_password(param['password']):
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token':token.key, 'user': serializer.data})


#This is a test item for creating events
@api_view(['GET'])
@csrf_protect
def getmodeldetails(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)


    return Response({'data': serializer.data})

#Get events a host has created
@api_view(['GET'])
@csrf_protect
def vieweventshost(request):
    params = request.query_params
    events = Event.objects.filter(event_host_user=params['event_host_user'])
    eventdata = EventSerializer(events, many=True)

    return Response({'data': eventdata.data})


#Get events an athlete has signed up for
@api_view(['GET'])
@csrf_protect
def vieweventsathlete(request):
    params = request.query_params

    participants = EventParticipant.objects.filter(username=params['username'])
    eventlist = []
    for i in range(len(participants.values())):
        eventlist.append(participants.values()[i]['event_name_id'])
    
    events = Event.objects.filter(event_id__in=eventlist)
    
    eventdata = EventSerializer(events, many=True)

    return Response({'data': eventdata.data})


#Get events a host has created
@api_view(['GET'])
@csrf_protect
def editeventshost(request):
    params = request.query_params
    event = get_object_or_404(Event, event_id=params['event_id'])
    if not event:
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = EventSerializer(instance=event)

    return Response({'data': serializer.data})