from django.shortcuts import render
# rest framework 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED
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

    try:
        user = User.objects.create_user(username=username, password=password)
        user.set_email = validate_email(username.lower())
        user.set_password = password
        user.save()
    except Exception as e:
        return Response({
            'msg' : 'Cdold not create user',
            'error': e.args
        })
    return Response({
        'msg': f'User {username} Created successfully',
    }, status=HTTP_201_CREATED)


# login
@api_view(['POST'])
def login_user(request: Request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is None:
        return Response({
            'msg': 'User not found, please check your username or password'
        })
    token = AccessToken.for_user(user)
    return Response({
        'msg': 'You are authenticated successfully',
        'token': str(token)
    })

# logout
@api_view(['POST'])
def logout_user(request: Request):
    logout(request)
    return Response({
        'msg': 'You are logged out successfully'
    })
