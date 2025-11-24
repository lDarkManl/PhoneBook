from django.urls import path
from . import views
from PhoneBook.views import export_subdivisions_excel

urlpatterns = [
    path('', views.SubdivisionListView.as_view(), name='subdivision_list'),
    path('export-excel/', export_subdivisions_excel, name='export_subdivisions_excel'),
    path('<int:pk>/tree/', views.subdivision_tree, name='subdivision_tree'),
]
