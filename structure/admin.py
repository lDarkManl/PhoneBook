from django.contrib import admin
from .models import TypeDivision, Location, Subdivision
@admin.register(TypeDivision)
class TDAdmin(admin.ModelAdmin):
    list_display = ('id','name')
@admin.register(Location)
class LocAdmin(admin.ModelAdmin):
    list_display = ('id','building','room')
@admin.register(Subdivision)
class SubAdmin(admin.ModelAdmin):
    list_display = ('id','name','id_type_division','id_location')
