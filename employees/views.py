from rest_framework import viewsets, filters
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer
from .forms import EmployeeForm
from positions.models import Post
from contacts.models import EmployeeDivision

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('role').all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname','name','middle_name']

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        queryset = Employee.objects.select_related('role').prefetch_related(
            'divisions__post', 'divisions__subdivision', 'divisions__subdivision__id_location'
        ).all()
        
        # Получаем параметры поиска
        search = self.request.GET.get('search', '').strip()
        filter_fio = self.request.GET.get('filter_fio')
        filter_post = self.request.GET.get('filter_post')
        filter_degree = self.request.GET.get('filter_degree')
        
        # Если есть поисковый запрос, применяем фильтры
        if search:
            query = Q()
            
            if filter_fio:
                query |= Q(surname__icontains=search) | Q(name__icontains=search) | Q(middle_name__icontains=search)
            
            if filter_post:
                query |= Q(divisions__post__name__icontains=search)
            
            if filter_degree:
                query |= Q(academic_degree__icontains=search)
            
            # Если ни один фильтр не выбран, ищем по всем полям
            if not any([filter_fio, filter_post, filter_degree]):
                query = (
                    Q(surname__icontains=search) |
                    Q(name__icontains=search) |
                    Q(middle_name__icontains=search) |
                    Q(divisions__post__name__icontains=search) |
                    Q(academic_degree__icontains=search)
                )
            
            queryset = queryset.filter(query).distinct()
        
        # Сортировка
        sort = self.request.GET.get('sort', 'asc')
        if sort == 'desc':
            queryset = queryset.order_by('-surname', '-name')
        else:
            queryset = queryset.order_by('surname', 'name')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
