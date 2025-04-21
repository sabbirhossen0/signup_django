from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Custumuser
from .serializers import UserSerializer


@api_view(['post'])
def register(request):
    data =request.data
    if Custumuser.objects.filter(username=data['username']).exists():
        return Response({'error','username already exists'},status=400),

    if Custumuser.objects.filter(email=data['email']).exists():
        return Response({'error','email already exists'},status=400),

    user = Custumuser.objects.create( 
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    
    serializer=UserSerializer(user)
    return Response(serializer.data)

@api_view(['post'])
def login_user(request):
    data=request.data

    try:
        user = Custumuser.objects.get(username=data['username'], password=data['password'])
        return Response({'message': 'Login successfully', 'user_id': user.id})
    except Custumuser.DoesNotExist:
        return Response({'error': 'Invalid username or password'}, status=400)