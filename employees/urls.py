from django.urls import path
from . import views
from PhoneBook.views import export_employees_excel

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('export-excel/', export_employees_excel, name='export_employees_excel'),
]
