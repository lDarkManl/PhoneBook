from django.shortcuts import render
from django.db.models import Q
from structure.models import Location
from events.models import Event
from .models import Schedule

def room_schedule(request):
    """Страница поиска и отображения расписания аудитории"""
    from datetime import date
    
    building = request.GET.get('building', '')
    room = request.GET.get('room', '')
    
    today_schedules = []
    today_events = []
    location = None
    buildings = Location.objects.values_list('building', flat=True).distinct().order_by('building')
    all_rooms = Location.objects.all().order_by('building', 'room')
    current_date = date.today()
    
    # Определяем текущий день недели (1=Понедельник, 7=Воскресенье)
    current_weekday = current_date.isoweekday()
    
    # Показываем расписание только если указаны оба параметра
    if building and room:
        # Ищем аудиторию
        try:
            location = Location.objects.get(building=building, room=room)
            
            # Получаем расписание занятий только на сегодня
            today_schedules = Schedule.objects.filter(
                location=location,
                weekday=current_weekday
            ).select_related('subject', 'lesson_type', 'teacher').order_by('start_time')
            
            # Получаем мероприятия в этой аудитории на сегодня
            today_events = Event.objects.filter(
                location=location,
                start_datetime__date=current_date
            ).select_related('type_event', 'organizer').order_by('start_datetime')
            
        except Location.DoesNotExist:
            pass
    
    context = {
        'buildings': buildings,
        'selected_building': building,
        'selected_room': room,
        'location': location,
        'today_schedules': today_schedules,
        'events': today_events,
        'all_rooms': all_rooms,
        'current_date': current_date,
    }
    
    return render(request, 'room_schedule.html', context)
