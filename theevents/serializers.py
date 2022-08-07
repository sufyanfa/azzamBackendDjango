from rest_framework.serializers import ModelSerializer
from .models import Event, Attendence

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AttendenceSerializer(ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'
        