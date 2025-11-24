from django.db import models
from structure.models import Location
from employees.models import Employee

class TypeEvent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self): return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='events')
    type_event = models.ForeignKey(TypeEvent, on_delete=models.PROTECT, related_name='events')
    organizer = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='events')
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    def __str__(self): return self.name
