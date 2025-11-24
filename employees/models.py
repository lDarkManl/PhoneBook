from django.db import models
from django.contrib.auth.models import User
from accounts.models import Role

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    academic_degree = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='employees')
    photo = models.ImageField(upload_to='employees/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.surname} {self.name}"
