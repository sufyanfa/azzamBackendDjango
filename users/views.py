from django.shortcuts import render
# rest framework 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
# user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# validate email
from django.core.validators import validate_email

# create user
@api_view(['POST'])
def register(request: Request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        validate_email(username)
    except:
        return Response({"error": "username is not a valid email"}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 8:
        return Response({"error": "password must be at least 8 characters"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password)
        user.set_email = validate_email(username.lower())
        user.set_password = password
        user.save()
    except Exception as e:
        return Response({
            'msg' : 'Cdold not create user',
            'error': e.args
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'msg': f'User {username} Created successfully',
    }, status=status.HTTP_201_CREATED)


# login
@api_view(['POST'])
def login_user(request: Request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is None:
        return Response({
            'msg': 'User not found, please check your username or password'
        }, status=status.HTTP_404_NOT_FOUND)

    token = AccessToken.for_user(user)
    return Response({
        'msg': 'You are authenticated successfully',
        'token': str(token)
    }, status=status.HTTP_200_OK)

# logout
@api_view(['POST'])
def logout_user(request: Request):
    logout(request)
    return Response({
        'msg': 'You are logged out successfully'
    }, status=status.HTTP_200_OK)
