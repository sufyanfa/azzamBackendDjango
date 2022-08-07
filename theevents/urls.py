from django.urls import path
from .views import create_event, add_attendences, get_event_details, delete_event, update_attendence, get_all_events_of_user_logged


app_name = 'theevents'

urlpatterns = [
    path('create-event/', create_event, name='create_event'),
    path('add-attendences/', add_attendences, name='add_attendences'),
    path('get-event-details/<id>/', get_event_details, name='get_event_details'),
    path('delete-event/<id>/', delete_event, name='delete_event'),
    path('update-attendence/<id>/', update_attendence, name='update_attendence'),
    path('get-all-events-of-user-logged/', get_all_events_of_user_logged, name='get_all_events_of_user_logged'),
]