from django.contrib import admin
from .models import TypeEvent, Event
@admin.register(TypeEvent)
class TEAdmin(admin.ModelAdmin):
    list_display = ('id','name')
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','start_datetime','end_datetime','location','type_event','organizer')
