from rest_framework import serializers
from .models import TypeEvent, Event

class TypeEventSerializer(serializers.ModelSerializer):
    class Meta: model=TypeEvent; fields='__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta: model=Event; fields='__all__'
