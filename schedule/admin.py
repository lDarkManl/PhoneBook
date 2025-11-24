from django.contrib import admin
from .models import Subject, LessonType, Schedule

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(LessonType)
class LessonTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['subject', 'lesson_type', 'teacher', 'location', 'weekday', 'start_time', 'end_time']
    list_filter = ['weekday', 'lesson_type', 'location']
    search_fields = ['subject__name', 'teacher__surname']
