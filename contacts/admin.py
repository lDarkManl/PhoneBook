from django.contrib import admin
from .models import EmployeeDivision
@admin.register(EmployeeDivision)
class EDAdmin(admin.ModelAdmin):
    list_display = ('id','employee','subdivision','post','internal_phone','city_phone','email')
    list_filter = ('subdivision','post')
