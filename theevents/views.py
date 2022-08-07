from django.shortcuts import render, get_object_or_404
from .models import Event, Attendence
from .serializers import EventSerializer, AttendenceSerializer
from rest_framework.response import Response
from rest_framework.request import Request
import pandas as pd

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# # create event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request):
    if request.method == 'POST':
        request.data['user'] = request.user.id
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)
    return Response(status=HTTP_403_FORBIDDEN)


# add attendences
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
            name = row['name']
            email = row['email']
            mobile = row['mobile']
            attendence = Attendence(
                event=event, name=name, email=email, mobile=mobile)
            attendence.save()
        return Response({"message": "Attendences added successfully."})



# get envet details & attendces, for user who is logged in and is the owner of the event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_event_details(request, id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=id)
        attendences = Attendence.objects.filter(event=event)
        serializer = EventSerializer(event)
        serializer2 = AttendenceSerializer(attendences, many=True)
        # count of attendences
        count = len(attendences)
        # count of attendees who will attend
        count_attendees_will_attend = len(attendences.filter(will_attend=True))
        # count of attendees who will not attend
        count_attendees_will_not_attend = len(attendences.filter(will_attend=False))
        # count of attendees who have attended
        count_attendees_have_attended = len(attendences.filter(is_attended=True))
        # count of attendees who have not attended
        count_attendees_have_not_attended = len(attendences.filter(is_attended=False))


        return Response({
            "event": serializer.data,
            "attendences": serializer2.data,
            "count": count,
            "count_attendees_will_attend": count_attendees_will_attend,
            "count_attendees_will_not_attend": count_attendees_will_not_attend,
            "count_attendees_have_attended": count_attendees_have_attended,
            "count_attendees_have_not_attended": count_attendees_have_not_attended
        })
    return Response(status=HTTP_403_FORBIDDEN)


