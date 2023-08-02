# urls.py
from django.urls import path
from .views import SendEventEmailsView

urlpatterns = [
    path('send_event_emails/', SendEventEmailsView.as_view(), name='send_event_emails'),
]
