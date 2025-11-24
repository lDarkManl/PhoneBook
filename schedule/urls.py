from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_schedule, name='room_schedule'),
]
