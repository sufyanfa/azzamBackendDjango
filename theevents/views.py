from django.shortcuts import render, get_object_or_404
from .models import Event, Attendence
from rest_framework.response import Response
from rest_framework.request import Request
import pandas as pd
from django.core.validators import validate_email

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# create event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        location = request.data.get('location')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        event = Event(name=name, description=description, location=location, start_date=start_date, end_date=end_date)
        event.save()
        return Response({"message": "Event created successfully."})
    
# add attendence from excel file
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_attendences(request):
    if request.method == 'POST':
        event_id = request.data.get('event_id')
        event = Event.objects.get(id=event_id)
        file = request.FILES['file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            if validate_email(row['email']) is not None:
                attendence = Attendence(event=event, name=row['name'], email=row['email'], mobile=row['mobile'])
                attendence.save()
            else:
                pass
        return Response({"message": "Attendences added successfully."})
    

# get envent details
@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def get_event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # events = [
    #     {'id': event.id, 'name': event.name, 'description': event.description, 'location': event.location, 'start_date': event.start_date, 'end_date': event.end_date}
    # ]

    contenxt = {
        'events': event
    }

    return render(request, 'theevents/event_details.html', contenxt)

