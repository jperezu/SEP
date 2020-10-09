import datetime
from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    organized_events = models.IntegerField(default=0)
    def __str__(self):
    	return self.client_name

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    description = models.CharField(max_length= 1000)
    attendees = models.IntegerField(default=0)
    expected_budget = models.IntegerField(default=0)
    from_date = models.DateTimeField('From')
    to_date = models.DateTimeField('To')
    decorations = models.CharField(max_length=500)
    film_and_photos = models.CharField(max_length=500)
    posters_art = models.CharField(max_length=500)
    food_drinks = models.CharField(max_length=500)
    music = models.CharField(max_length=500)
    computers = models.CharField(max_length=500)
    other = models.CharField(max_length=500)
    status = models.CharField(max_length=20)

    def __str__(self):
        return  '%s\'s %s' % (self.client, self.event_type)

class RequestEvent(models.Model):
    client = models.CharField(max_length=20)
    event_type = models.CharField(max_length=200)
    description = models.CharField(max_length= 1000)
    attendees = models.IntegerField(default=0)
    expected_budget = models.IntegerField(default=0)
    from_date = models.DateTimeField('From')
    to_date = models.DateTimeField('To')
    decorations = models.CharField(max_length=500)
    film_and_photos = models.CharField(max_length=500)
    posters_art = models.CharField(max_length=500)
    food_drinks = models.CharField(max_length=500)
    music = models.CharField(max_length=500)
    computers = models.CharField(max_length=500)
    other = models.CharField(max_length=500)
    status = models.CharField(max_length=20)

    def __str__(self):
        return  '%s\'s request' % self.client