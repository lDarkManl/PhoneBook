from rest_framework import serializers
from .models import EmployeeDivision
from employees.serializers import EmployeeSerializer
from structure.serializers import SubdivisionSerializer
from positions.serializers import PostSerializer

class EmployeeDivisionSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    subdivision = SubdivisionSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = EmployeeDivision
        fields = '__all__'
