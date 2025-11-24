from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User
from accounts.serializers import RoleSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ['id','surname','name','middle_name','academic_degree','role','user']
