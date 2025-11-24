from rest_framework import viewsets, filters
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import EmployeeDivision
from .serializers import EmployeeDivisionSerializer
from .forms import EmployeeDivisionForm
from structure.models import Subdivision
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeDivisionViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDivision.objects.select_related('employee','subdivision','post').all()
    serializer_class = EmployeeDivisionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['subdivision','post']
    search_fields = ['internal_phone','city_phone','email','employee__surname','employee__name']

class ContactListView(ListView):
    model = EmployeeDivision
    template_name = 'contact_list.html'
    context_object_name = 'contacts'
    
    def get_queryset(self):
        queryset = EmployeeDivision.objects.select_related('employee', 'subdivision', 'post').all()
        search = self.request.GET.get('search')
        subdivision = self.request.GET.get('subdivision')
        
        if search:
            queryset = queryset.filter(
                Q(employee__surname__icontains=search) |
                Q(employee__name__icontains=search) |
                Q(internal_phone__icontains=search) |
                Q(city_phone__icontains=search) |
                Q(email__icontains=search)
            )
        if subdivision:
            queryset = queryset.filter(subdivision_id=subdivision)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subdivisions'] = Subdivision.objects.all()
        return context

class ContactCreateView(CreateView):
    model = EmployeeDivision
    form_class = EmployeeDivisionForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = EmployeeDivision
    form_class = EmployeeDivisionForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = EmployeeDivision
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')
