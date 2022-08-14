from django.shortcuts import render, get_object_or_404
from .models import Event, Attendence
from .serializers import EventSerializer, AttendenceSerializer
from rest_framework.response import Response
from rest_framework.request import Request
import pandas as pd
from django.core.validators import validate_email

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


# add attendences
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_attendences(request):
    valid_emails = 0
    if request.method == 'POST':
        event_id = request.data.get('event_id')
        event = Event.objects.get(id=event_id)
        file = request.FILES['file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            name = row['name']
            email = row['email']
            # check if email is null
            mobile = row['mobile']
            attendence = Attendence(
                event=event, name=name, email=email, mobile=mobile)
            attendence.save()

        # check if email is valid
        for index, row in df.iterrows():
            email = row['email']
            try:
                validate_email(email)
                valid_emails += 1
            except:
                pass
        return Response({"message": "Attendences added successfully.", "valid_emails": valid_emails}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)



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

        statistics_dict = {
            "count": count,
            "count_attendees_will_attend": count_attendees_will_attend,
            "count_attendees_will_not_attend": count_attendees_will_not_attend,
            "count_attendees_have_attended": count_attendees_have_attended,
            "count_attendees_have_not_attended": count_attendees_have_not_attended
        }

        return Response({"event": serializer.data, "attendences": serializer2.data, "statistics": statistics_dict}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


# delete event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_event(request, id):
    # only the owner of the event can delete the event
    if request.method == 'POST':
        event = get_object_or_404(Event, id=id)
        if event.user == request.user:
            event.delete()
            return Response({"message": "Event deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You are not authorized to delete this event."}, status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

# update event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_event(request, id):
    # only the owner of the event can update the event
    if request.method == 'POST':
        event = get_object_or_404(Event, id=id)
        if event.user == request.user:
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


# update attendence
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_attendence(request, id):
    # only the owner of the event can update the event
    if request.method == 'POST':
        attendence = get_object_or_404(Attendence, id=id)
        if attendence.event.user == request.user:
            serializer = AttendenceSerializer(attendence, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

    



# delete attendence
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_attendence(request, id):
    # only the owner of the event can delete the attendence
    if request.method == 'POST':
        attendence = get_object_or_404(Attendence, id=id)
        if attendence.user == request.user:
            attendence.delete()
            return Response({"message": "Attendence deleted successfully."})
        return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


# delete all attendences of an event
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_all_attendences(request, id):
    # only the owner of the event can delete the attendences
    if request.method == 'POST':
        event = get_object_or_404(Event, id=id)
        if event.user == request.user:
            attendences = Attendence.objects.filter(event=event)
            attendences.delete()
            return Response({"message": "Attendences deleted successfully."}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)




# get all events for user who is logged in
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_all_events_of_user_logged(request):
    if request.method == 'POST':
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)