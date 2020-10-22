import datetime
from django.test import TestCase, TransactionTestCase, Client
from django.db import models
from SEP.models import Client, Event, RequestEvent, RequestRecruitment, RequestBudget, Task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

#from django import models

# Create your tests here.
class ClientTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(client_name ='Big Boss', organized_events ='10')

    def test_client_name_max_length(self):
        #This test max length of client name is 50.
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('client_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_client_name(self):
       #This tests object name is same as implemented. 
       client = Client.objects.get(id=1)
       expected_object_name =  client.client_name
       self.assertEquals(expected_object_name, str(client))

class EventTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')

    def test_client_name_label(self):
        # This test is testing client name label is in the right place.
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('client').verbose_name
        self.assertEquals(field_label, 'client')

    def test_decorations_max_length(self):
        # This test checkes the max length of decoration is same as designed.
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('decorations').max_length
        self.assertEquals(max_length, 500)

    def test_object_name_is_client_and_event_type(self):
        # This checks the object name is correct. 
       Client.objects.create(client_name ='Big Boss', organized_events ='10')
       client = Client.objects.get(id=1)
       event = Event.objects.get(id=1)
       expected_object_name =  '%s\'s %s' % (event.client, event.event_type)
       self.assertEquals(expected_object_name, str(event))
    


class RequestEventTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test method
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        RequestEvent.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
   
    def test_client_name_label(self):
        # This test client name's label is correct.
        requestevent = RequestEvent.objects.get(id=1)
        field_label = requestevent._meta.get_field('client').verbose_name
        self.assertEquals(field_label, 'client')


    def test_description_max_length(self):
        # This test checkes the max length of description is same as designed.
        requestevent = RequestEvent.objects.get(id=1)
        max_length = requestevent._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_client_name_and_event_type(self):
        # This checks the object name is correct. 
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        requestevent = RequestEvent.objects.get(id=1)
        expected_object_name =  '%s\'s request' % client
        self.assertEquals(expected_object_name, str(requestevent))


class RequestRecruitmentTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test method
        RequestRecruitment.objects.create(type ='Co-work with Subteam', department ='Subteam', experience ='Professional', job ='DJ', description ='Customer wants marshmellow for this event', status ='on going')    


    def test_description_max_length(self):
        # This test checkes the max length of description is same as designed.
        recruitment = RequestRecruitment.objects.get(id=1)
        max_length = recruitment._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)
        
    def test_object_name_is_job_and_department(self):
        # This checks the object name is correct. 
       recruitment = RequestRecruitment.objects.get(id=1)
       expected_object_name =  '%s\' for %s' % (recruitment.job, recruitment.department)
       self.assertEquals(expected_object_name, str(recruitment))


class RequestBudgetTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test method
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
        event = Event.objects.get(id=1)
        RequestBudget.objects.create(project=event, department ='Service Team' , budget = '500', description='more balloons', status = 'on going')
    
    def test_description_max_length(self):
        # This test checkes the max length of description is same as designed.
        budget = RequestBudget.objects.get(id=1)
        max_length = budget._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_object_name_is_department(self):
        # This checks the object name is correct. 
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
        event = Event.objects.get(id=1)
        budget = RequestBudget.objects.get(id=1)
        expected_object_name ='%s budget request' % (budget.department)
        self.assertEquals(expected_object_name, str(budget))

class TaskTest(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        # Set up non-modified objects used by all test method
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
        event = Event.objects.get(id=1)
        User.objects.create(username='admin', password='pass@123', email='admin@admin.com')
        assigned = User.objects.get(id=1)
        User.objects.create(username='admin1', password='pass@123', email='admin1@admin.com')
        assigner = User.objects.get(id=1)
        Task.objects.create(project=event, description='500 dishes of stake', assigned =assigned, assigner =assigner , priority = 'High', status ='on going')
    
    def test_description_max_length(self):
        # This test checkes the max length of description is same as designed.
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('status').max_length
        self.assertEquals(max_length, 20)

    def test_object_name_is_department(self):
        # This checks the object name is correct. 
        Client.objects.create(client_name ='Big Boss', organized_events ='10')
        client = Client.objects.get(id=1)
        Event.objects.create(client=client, event_type ='Charity Party', description ='It will be a fun party', attendees ='50', expected_budget ='5000', from_date ='2020-10-10', to_date ='2020-10-13', decorations ='ballons', film_and_photos ='10 mins video, 1000 photos', posters_art ='10 posters', food_drinks ='Wine and cheese', music ='Classic and american pop songs', computers ='3 computers', other ='Consult with every details with the customer', status = 'suspend')
        event = Event.objects.get(id=1)
        task = Task.objects.get(id=1)
        expected_object_name ='Task for %s' % task.assigned.first_name
        self.assertEquals(expected_object_name, str(task))


   