from rest_framework import serializers
from .models import Employee, Event

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Event
        fields = '__all__'