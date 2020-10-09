import datetime
from django.test import TestCase
from django.db import models
from SEP.models import Client
from SEP.models import Event
from SEP.models import RequestEvent
#from django import models

# Create your tests here.
class ClientTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(client_name ='Big Boss', organized_events ='10')


 

    def test_client_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('client_name').max_length
        self.assertEquals(max_length, 50)


class EventTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')

    def test_client_name_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('client').verbose_name
        self.assertEquals(field_label, 'client')



    def test_decorations_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('decorations').max_length
        self.assertEquals(max_length, 500)

    
    


class RequestEventTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test method
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        RequestEvent.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
    def test_client_name_label(self):
        requestevent = RequestEvent.objects.get(id=1)
        field_label = requestevent._meta.get_field('client').verbose_name
        self.assertEquals(field_label, 'client')


    def test_decorations_max_length(self):
        requestevent = RequestEvent.objects.get(id=1)
        max_length = requestevent._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_client_name_and_event_type(self):
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        requestevent = RequestEvent.objects.get(id=1)
        expected_object_name =  '%s\'s request' % client
        self.assertEquals(expected_object_name, str(requestevent))

