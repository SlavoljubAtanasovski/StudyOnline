from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer
from .random_n_digit import random_with_N_digits
from config import settings

@api_view(['POST'])
def signup(request):
    email = request.data.get('email', False)
    password = request.data.get('password', False)
    first_name = request.data.get('first_name', False)
    last_name = request.data.get('last_name', False)
    if User.objects.filter(email=email).exists():
        return Response(data="Email already in use.", status=409)
    else:
        user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        subject = "Please confirm your email"
        number = random_with_N_digits(6)
        user.auth_code = str(number)
        user.save()
        email_template_name = "registration_verification.html"
        html_message = render(request, email_template_name, {'auth_code': number}).content.decode('utf-8')
        # url_link = "http://localhost:8000/user/auth/{}/verify/{}".format(user.id, number)
        message = "This is the email from online language school. This is authentication code.\r\n {}".format(number)
        user.email_user(subject, message, from_email=settings.EMAIL_HOST_USER, html_message=html_message)
        return Response(status=201)
    
@api_view(['POST'])
def signin(request):
    email = request.data.get('email', False)
    password = request.data.get('password', False)
    user = authenticate(email=email, password=password)
    user_serialized = UserSerializer(user)
    if user is not None:
        login(request, user)
        return Response(user_serialized.data)
    else:
        return Response(data="Something is wrong.", status=404)

@api_view(['POST'])
def authorize(request):
    email = request.data.get('email', False)
    key = request.data.get('key', False)
    user = User.objects.get(email=email)
    original_key = user.auth_code
    if user is not None and key == original_key:
        user.is_active = True
        user.save()
        login(request, user)
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)
    else:
        return Response(data="Something is wrong.", status=404)

@api_view(['GET'])
def email_authorize(request, id, key):
    user = User.objects.get(id=id)
    original_key = user.auth_code
    if user is not None and key == original_key:
        user.is_active = True
        user.save()
        login(request, user)
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)
    else:
        return Response(data="Something is wrong.", status=404)

# @login_required
@api_view(['POST'])
def signout(request):
    logout(request)
    return Response(status=200)
