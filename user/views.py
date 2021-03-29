from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

@api_view(['POST', 'GET'])
def signup(request):
    print(request.data)
    email = request.data.get('email', False)
    password = request.data.get('password', False)
    print(email)
    print(password)
    first_name = request.data.get('first_name', False)
    last_name = request.data.get('last_name', False)
    if User.objects.filter(email=email).exists():
        return Response(data="Email already in use.", status=409)
    else:
        User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        return Response(status=201)
    
@api_view(['POST', 'GET'])
def signin(request):
    email = request.data.get('email', False)
    password = request.data.get('password', False)
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        return Response(status=200)
    else:
        return "Something is wrong.", 404