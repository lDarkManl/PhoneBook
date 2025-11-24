from django import forms
from .models import Subdivision

class SubdivisionForm(forms.ModelForm):
    class Meta:
        model = Subdivision
        fields = ['name', 'id_type_division', 'id_location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_type_division': forms.Select(attrs={'class': 'form-select'}),
            'id_location': forms.Select(attrs={'class': 'form-select'}),
        }
