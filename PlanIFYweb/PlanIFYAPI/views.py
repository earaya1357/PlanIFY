from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import EventSerializer, UserAccountSerializer, UserSerializer
from .models import Event, UserAccount
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def dashboarddata(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def createevent(request):
    event = EventSerializer(data=request.data)
    if event.is_valid():
        event.save()

    return Response(event.data)

@api_view(['GET'])
def useraccount(request):
    param = request.query_params
    user = get_object_or_404(UserAccount, username=param['id'])
    if not user:
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserAccountSerializer(instance=user)

    return Response({'user': serializer.data})

@api_view(['GET'])
def user(request):
    param = request.query_params
    user = get_object_or_404(User, username=param['username'])
    if not user.check_password(param['password']):
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token':token.key, 'user': serializer.data})
