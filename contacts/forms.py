from django import forms
from .models import EmployeeDivision

class EmployeeDivisionForm(forms.ModelForm):
    class Meta:
        model = EmployeeDivision
        fields = ['employee', 'subdivision', 'post', 'internal_phone', 'city_phone', 'email']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'subdivision': forms.Select(attrs={'class': 'form-select'}),
            'post': forms.Select(attrs={'class': 'form-select'}),
            'internal_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
