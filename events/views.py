from rest_framework import viewsets, filters
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import TypeEvent, Event
from .serializers import *
from .forms import EventForm

class TypeEventViewSet(viewsets.ModelViewSet):
    queryset = TypeEvent.objects.all()
    serializer_class = TypeEventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related('location','type_event','organizer').all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        queryset = Event.objects.select_related('location', 'type_event', 'organizer').all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
