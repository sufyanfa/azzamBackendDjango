from django.contrib import admin
from .models import Event, Attendence

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('name', 'description', 'location', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'location', 'start_date', 'end_date', 'created_at', 'updated_at')

@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email', 'mobile', 'status', 'created_at', 'updated_at')
    list_filter = ('event', 'name', 'email', 'mobile', 'status', 'created_at', 'updated_at')
    search_fields = ('event', 'name', 'email', 'mobile', 'status', 'created_at', 'updated_at')