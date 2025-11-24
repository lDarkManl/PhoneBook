from rest_framework import viewsets, filters
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import TypeDivision, Location, Subdivision
from .serializers import *
from .forms import SubdivisionForm
from contacts.models import EmployeeDivision

class TypeDivisionViewSet(viewsets.ModelViewSet):
    queryset = TypeDivision.objects.all()
    serializer_class = TypeDivisionSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class SubdivisionViewSet(viewsets.ModelViewSet):
    queryset = Subdivision.objects.select_related('id_type_division','id_location').all()
    serializer_class = SubdivisionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class SubdivisionListView(ListView):
    """Список только факультетов (родительских подразделений)"""
    model = Subdivision
    template_name = 'subdivision_list.html'
    context_object_name = 'subdivisions'
    
    def get_queryset(self):
        from django.db.models import Q
        
        # Получаем только факультеты (подразделения без родителя)
        queryset = Subdivision.objects.filter(
            parent__isnull=True
        ).select_related(
            'id_type_division', 'id_location'
        ).prefetch_related('employees', 'children')
        
        # Поиск
        search = self.request.GET.get('search', '').strip()
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(id_location__building__icontains=search) |
                Q(id_location__room__icontains=search)
            )
        
        queryset = queryset.all()
        
        # Добавляем информацию о руководителе для каждого факультета
        subdivisions_with_heads = []
        for subdivision in queryset:
            # Ищем декана
            head = subdivision.employees.filter(
                post__name__iregex=r'(декан|директор|руководитель)'
            ).select_related('employee', 'post').first()
            subdivision.head = head
            subdivisions_with_heads.append(subdivision)
        
        return subdivisions_with_heads

def subdivision_tree(request, pk):
    """Дерево подразделений - показывает кафедры факультета"""
    faculty = get_object_or_404(Subdivision, pk=pk)
    
    # Ищем декана факультета
    faculty_head = faculty.employees.filter(
        post__name__iregex=r'(декан|директор|руководитель)'
    ).select_related('employee', 'post').first()
    faculty.head = faculty_head
    
    # Получаем все дочерние подразделения (кафедры)
    departments = Subdivision.objects.filter(
        parent=faculty
    ).select_related(
        'id_type_division', 'id_location'
    ).prefetch_related('employees__employee', 'employees__post')
    
    # Добавляем информацию о руководителе для каждой кафедры
    departments_with_heads = []
    for department in departments:
        # Ищем заведующего кафедрой
        head = department.employees.filter(
            post__name__iregex=r'(заведующий|руководитель|начальник)'
        ).select_related('employee', 'post').first()
        department.head = head
        departments_with_heads.append(department)
    
    context = {
        'faculty': faculty,
        'departments': departments_with_heads,
    }
    return render(request, 'subdivision_tree.html', context)

class SubdivisionDetailView(DetailView):
    model = Subdivision
    template_name = 'subdivision_detail.html'
    context_object_name = 'subdivision'

class SubdivisionCreateView(CreateView):
    model = Subdivision
    form_class = SubdivisionForm
    template_name = 'subdivision_form.html'
    success_url = reverse_lazy('subdivision_list')

class SubdivisionUpdateView(UpdateView):
    model = Subdivision
    form_class = SubdivisionForm
    template_name = 'subdivision_form.html'
    success_url = reverse_lazy('subdivision_list')

class SubdivisionDeleteView(DeleteView):
    model = Subdivision
    template_name = 'subdivision_confirm_delete.html'
    success_url = reverse_lazy('subdivision_list')
