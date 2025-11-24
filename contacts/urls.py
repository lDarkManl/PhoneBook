from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
