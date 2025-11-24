from rest_framework import serializers
from .models import TypeDivision, Location, Subdivision

class TypeDivisionSerializer(serializers.ModelSerializer):
    class Meta: model = TypeDivision; fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta: model = Location; fields = '__all__'

class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta: model = Subdivision; fields = '__all__'
