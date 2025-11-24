from django.db import models
from employees.models import Employee
from structure.models import Subdivision
from positions.models import Post

class EmployeeDivision(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='divisions')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.PROTECT, related_name='employees')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='holders')
    internal_phone = models.CharField(max_length=50, blank=True, null=True)
    city_phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('employee','subdivision','post')
    def __str__(self):
        return f"{self.employee} @ {self.subdivision}"
