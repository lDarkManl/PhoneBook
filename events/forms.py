from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_datetime', 'end_datetime', 'location', 'type_event', 'organizer', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'type_event': forms.Select(attrs={'class': 'form-select'}),
            'organizer': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
