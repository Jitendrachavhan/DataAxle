# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from datetime import date
from .serializers import EmployeeSerializer, EventSerializer
class SendEventEmailsView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        current_date = date.today()
        events = Event.objects.filter(event_date__date=current_date, email_sent=False)
        
        if not events:
            # No events scheduled for the current period
            return Response({'message': 'No events scheduled for the current period.'}, status=status.HTTP_200_OK)

        for event in events:
            try:
                email_template = get_email_template(event.event_type)
                if email_template:
                    email_content = render_email_template(email_template, event.employee)
                    send_email(event.employee.email, f"Special Event: {event.event_type.capitalize()}", email_content)
                    event.email_sent = True
                    event.save()

                    log_email_status(event, 'Success')

            except Exception as e:
                log_email_status(event, 'Failed', error_message=str(e))

        return Response({'message': 'Event emails sent successfully.'}, status=status.HTTP_200_OK)

def get_email_template(event_type):
    # Assuming you have stored email templates in the Django database as per the event type
    # You can modify this function according to your template storage method
    # For simplicity, I'm using a dictionary here
    email_templates = {
        'birthday': 'birthday_email_template.html',
        'work_anniversary': 'work_anniversary_email_template.html'
    }
    return email_templates.get(event_type)

def render_email_template(template_name, employee):
    # Implement the logic to render the email template here
    # You can use Django template rendering or any other method of your choice
    # For simplicity, I'm returning a placeholder string here
    return f"Hello {employee.name},\n\nThis is a placeholder email content for {template_name}."

def send_email(recipient_email, subject, content):
    # Implement the logic to send emails here
    # You can use Django's send_mail() or any other email library of your choice
    # For simplicity, I'm printing the email content to console
    print(f"Sending email to: {recipient_email}\nSubject: {subject}\nContent:\n{content}")

def log_email_status(event, status, error_message=None):
    # Log the email status and error message (if any) in the Django database
    # You can use Django's models to create a new EmailLog entry
    # For simplicity, I'm printing the status and error message to console
    print(f"Logging email status for event ID {event.id}: {status}")
    if error_message:
        print(f"Error message: {error_message}")
