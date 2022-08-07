from django.contrib import admin
from .models import Event, Attendence, User

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'is_online', 'is_active', 'is_certified', 'online_link', 'description', 'file_link', 'organizetion', 'address', 'city', 'location', 'start_date', 'end_date', 'num_of_attendees', 'user', 'created_at', 'updated_at')
    list_filter = ('is_online', 'is_active', 'is_certified')
    search_fields = ('name', 'description', 'organizetion', 'address', 'city', 'location', 'start_date', 'end_date', 'num_of_attendees', 'user')
    list_per_page = 25
    

@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email', 'mobile', 'is_attended', 'will_attend', 'created_at', 'updated_at')
    list_filter = ('is_attended', 'will_attend')
    search_fields = ('event', 'name', 'email', 'mobile')
    list_per_page = 25


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 25
    ordering = ('user',)