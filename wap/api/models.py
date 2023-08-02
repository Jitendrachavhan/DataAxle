from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Event(models.Model):
    event_types = (
        ('birthday', 'Birthday'),
        ('work_anniversary', 'Work Anniversary')
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(choices=event_types, max_length=20)
    event_date = models.DateField()
    email_sent = models.BooleanField(default=False)