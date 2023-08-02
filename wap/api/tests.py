# tests.py
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employee, Event

class EventEmailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee1 = Employee.objects.create(name='John Doe', email='john.doe@example.com')
        self.employee2 = Employee.objects.create(name='Jane Smith', email='jane.smith@example.com')

        #self.event1 = Event.objects.create(employee=self.employee1, event_type='birthday', event_date=date.today())
        #self.event2 = Event.objects.create(employee=self.employee2, event_type='work_anniversary', event_date=date.today())
        #self.future_event = Event.objects.create(employee=self.employee1, event_type='birthday', event_date=date.today() + timedelta(days=30))

    def test_send_event_emails(self):
        url = '/send_event_emails/'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.filter(email_sent=True).count(), 2)

    def test_no_events_scheduled(self):
        url = '/send_event_emails/'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.filter(email_sent=True).count(), 2)

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_email_sending_exception(self):
        # Assuming an email sending exception occurs for event1
        #self.event1.event_date = date.today()
        self.event1.save()

        url = '/send_event_emails/'
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.filter(email_sent=True).count(), 1)
