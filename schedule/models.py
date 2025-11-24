from django.db import models
from structure.models import Location
from employees.models import Employee

class Subject(models.Model):
    """Предмет"""
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class LessonType(models.Model):
    """Тип занятия"""
    name = models.CharField(max_length=100)  # Лекция, Практика, Лабораторная работа
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    """Расписание занятий"""
    WEEKDAYS = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
    ]
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='schedules')
    lesson_type = models.ForeignKey(LessonType, on_delete=models.PROTECT, related_name='schedules')
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='schedules')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='schedules')
    weekday = models.IntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        ordering = ['weekday', 'start_time']
    
    def __str__(self):
        return f"{self.subject.name} - {self.get_weekday_display()} {self.start_time}"
