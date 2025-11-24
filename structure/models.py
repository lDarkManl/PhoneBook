from django.db import models

class TypeDivision(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self): return self.name

class Location(models.Model):
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    def __str__(self): return f"{self.building}/{self.room}"

class Subdivision(models.Model):
    name = models.CharField(max_length=200)
    id_type_division = models.ForeignKey(TypeDivision, on_delete=models.PROTECT, related_name='subdivisions')
    id_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='subdivisions')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self): return self.name
