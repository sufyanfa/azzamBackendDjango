from django.urls import path
from .views import create_event, add_attendences, get_event_details


app_name = 'theevents'

urlpatterns = [
    path('create-event/', create_event, name='create_event'),
    path('add-attendences/', add_attendences, name='add_attendences'),
    path('get-event-details/<pk>/', get_event_details, name='get_event_details'),
]
