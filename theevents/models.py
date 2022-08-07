from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events_images/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_certified = models.BooleanField(default=False)
    online_link = models.URLField(blank=True)
    description = models.TextField()
    file_link = models.URLField(blank=True, null=True)
    organizetion = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    num_of_attendees = models.IntegerField(default=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Attendence(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20)
    is_attended = models.BooleanField(default=False)
    will_attend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


# add mobile number to user model
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username