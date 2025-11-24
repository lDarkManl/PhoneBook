"""
Скрипт для наполнения базы данных тестовыми данными
Запуск: python populate_db.py
"""
import os
import django
import sys

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PhoneBook.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Role
from employees.models import Employee
from structure.models import TypeDivision, Location, Subdivision
from positions.models import Post
from contacts.models import EmployeeDivision
from events.models import TypeEvent, Event
from datetime import datetime, timedelta

def populate():
    print("Начинаем наполнение базы данных...")
    
    # Создаем роли
    print("\n1. Создание ролей...")
    role_admin, _ = Role.objects.get_or_create(name="Администратор")
    role_teacher, _ = Role.objects.get_or_create(name="Преподаватель")
    role_staff, _ = Role.objects.get_or_create(name="Сотрудник")
    print(f"   Создано ролей: {Role.objects.count()}")
    
    # Создаем типы подразделений
    print("\n2. Создание типов подразделений...")
    type_faculty, _ = TypeDivision.objects.get_or_create(name="Факультет")
    type_department, _ = TypeDivision.objects.get_or_create(name="Кафедра")
    type_lab, _ = TypeDivision.objects.get_or_create(name="Лаборатория")
    print(f"   Создано типов: {TypeDivision.objects.count()}")
    
    # Создаем локации (аудитории)
    print("\n3. Создание локаций...")
    locations = [
        Location.objects.get_or_create(building="Корпус 1", room="101")[0],
        Location.objects.get_or_create(building="Корпус 1", room="102")[0],
        Location.objects.get_or_create(building="Корпус 1", room="103")[0],
        Location.objects.get_or_create(building="Корпус 1", room="205")[0],
        Location.objects.get_or_create(building="Корпус 1", room="206")[0],
        Location.objects.get_or_create(building="Корпус 1", room="301")[0],
        Location.objects.get_or_create(building="Корпус 2", room="101")[0],
        Location.objects.get_or_create(building="Корпус 2", room="201")[0],
        Location.objects.get_or_create(building="Корпус 2", room="301")[0],
        Location.objects.get_or_create(building="Корпус 2", room="405")[0],
        Location.objects.get_or_create(building="Корпус 3", room="102")[0],
        Location.objects.get_or_create(building="Корпус 3", room="210")[0],
        Location.objects.get_or_create(building="Корпус 3", room="305")[0],
        Location.objects.get_or_create(building="Корпус 3", room="401")[0],
    ]
    print(f"   Создано локаций: {Location.objects.count()}")
    
    # Создаем должности
    print("\n4. Создание должностей...")
    posts = {
        'dean': Post.objects.get_or_create(name="Декан факультета")[0],
        'head_dept': Post.objects.get_or_create(name="Заведующий кафедрой")[0],
        'professor': Post.objects.get_or_create(name="Профессор")[0],
        'assoc_prof': Post.objects.get_or_create(name="Доцент")[0],
        'senior_lect': Post.objects.get_or_create(name="Старший преподаватель")[0],
        'assistant': Post.objects.get_or_create(name="Ассистент")[0],
    }
    print(f"   Создано должностей: {Post.objects.count()}")
    
    # Создаем подразделения
    print("\n5. Создание подразделений...")
    subdivisions = []
    
    # Факультеты
    faculty_it = Subdivision.objects.get_or_create(
        name="Факультет информационных технологий",
        id_type_division=type_faculty,
        id_location=locations[0]
    )[0]
    subdivisions.append(faculty_it)
    
    faculty_math = Subdivision.objects.get_or_create(
        name="Математический факультет",
        id_type_division=type_faculty,
        id_location=locations[1]
    )[0]
    subdivisions.append(faculty_math)
    
    faculty_physics = Subdivision.objects.get_or_create(
        name="Физический факультет",
        id_type_division=type_faculty,
        id_location=locations[2]
    )[0]
    subdivisions.append(faculty_physics)
    
    # Кафедры (привязываем к факультетам)
    dept_programming = Subdivision.objects.get_or_create(
        name="Кафедра программирования",
        id_type_division=type_department,
        id_location=locations[3],
        defaults={'parent': faculty_it}
    )[0]
    if not dept_programming.parent:
        dept_programming.parent = faculty_it
        dept_programming.save()
    subdivisions.append(dept_programming)
    
    dept_networks = Subdivision.objects.get_or_create(
        name="Кафедра компьютерных сетей",
        id_type_division=type_department,
        id_location=locations[4],
        defaults={'parent': faculty_it}
    )[0]
    if not dept_networks.parent:
        dept_networks.parent = faculty_it
        dept_networks.save()
    subdivisions.append(dept_networks)
    
    dept_algebra = Subdivision.objects.get_or_create(
        name="Кафедра алгебры и геометрии",
        id_type_division=type_department,
        id_location=locations[5],
        defaults={'parent': faculty_math}
    )[0]
    if not dept_algebra.parent:
        dept_algebra.parent = faculty_math
        dept_algebra.save()
    subdivisions.append(dept_algebra)
    
    print(f"   Создано подразделений: {Subdivision.objects.count()}")
    
    # Создаем сотрудников
    print("\n6. Создание сотрудников...")
    employees_data = [
        # Деканы
        {
            'surname': 'Иванов', 'name': 'Иван', 'middle_name': 'Иванович',
            'academic_degree': 'д.т.н.', 'role': role_teacher,
            'subdivision': faculty_it, 'post': posts['dean'],
            'internal_phone': '1001', 'city_phone': '+7 (495) 123-45-01',
            'email': 'ivanov@university.ru'
        },
        {
            'surname': 'Петрова', 'name': 'Мария', 'middle_name': 'Сергеевна',
            'academic_degree': 'д.ф.-м.н.', 'role': role_teacher,
            'subdivision': faculty_math, 'post': posts['dean'],
            'internal_phone': '1002', 'city_phone': '+7 (495) 123-45-02',
            'email': 'petrova@university.ru'
        },
        {
            'surname': 'Сидоров', 'name': 'Петр', 'middle_name': 'Александрович',
            'academic_degree': 'д.ф.-м.н.', 'role': role_teacher,
            'subdivision': faculty_physics, 'post': posts['dean'],
            'internal_phone': '1003', 'city_phone': '+7 (495) 123-45-03',
            'email': 'sidorov@university.ru'
        },
        # Заведующие кафедрами
        {
            'surname': 'Козлов', 'name': 'Дмитрий', 'middle_name': 'Викторович',
            'academic_degree': 'к.т.н.', 'role': role_teacher,
            'subdivision': dept_programming, 'post': posts['head_dept'],
            'internal_phone': '2001', 'city_phone': '+7 (495) 123-46-01',
            'email': 'kozlov@university.ru'
        },
        {
            'surname': 'Смирнова', 'name': 'Елена', 'middle_name': 'Павловна',
            'academic_degree': 'к.т.н.', 'role': role_teacher,
            'subdivision': dept_networks, 'post': posts['head_dept'],
            'internal_phone': '2002', 'city_phone': '+7 (495) 123-46-02',
            'email': 'smirnova@university.ru'
        },
        {
            'surname': 'Новиков', 'name': 'Андрей', 'middle_name': 'Михайлович',
            'academic_degree': 'д.ф.-м.н.', 'role': role_teacher,
            'subdivision': dept_algebra, 'post': posts['head_dept'],
            'internal_phone': '2003', 'city_phone': '+7 (495) 123-46-03',
            'email': 'novikov@university.ru'
        },
        # Профессора
        {
            'surname': 'Волков', 'name': 'Сергей', 'middle_name': 'Николаевич',
            'academic_degree': 'д.т.н.', 'role': role_teacher,
            'subdivision': dept_programming, 'post': posts['professor'],
            'internal_phone': '3001', 'city_phone': '+7 (495) 123-47-01',
            'email': 'volkov@university.ru'
        },
        {
            'surname': 'Морозова', 'name': 'Ольга', 'middle_name': 'Владимировна',
            'academic_degree': 'д.ф.-м.н.', 'role': role_teacher,
            'subdivision': dept_algebra, 'post': posts['professor'],
            'internal_phone': '3002', 'city_phone': '+7 (495) 123-47-02',
            'email': 'morozova@university.ru'
        },
        # Доценты
        {
            'surname': 'Лебедев', 'name': 'Алексей', 'middle_name': 'Игоревич',
            'academic_degree': 'к.т.н.', 'role': role_teacher,
            'subdivision': dept_programming, 'post': posts['assoc_prof'],
            'internal_phone': '4001', 'city_phone': '+7 (495) 123-48-01',
            'email': 'lebedev@university.ru'
        },
        {
            'surname': 'Соколова', 'name': 'Анна', 'middle_name': 'Дмитриевна',
            'academic_degree': 'к.т.н.', 'role': role_teacher,
            'subdivision': dept_networks, 'post': posts['assoc_prof'],
            'internal_phone': '4002', 'city_phone': '+7 (495) 123-48-02',
            'email': 'sokolova@university.ru'
        },
        {
            'surname': 'Попов', 'name': 'Владимир', 'middle_name': 'Сергеевич',
            'academic_degree': 'к.ф.-м.н.', 'role': role_teacher,
            'subdivision': dept_algebra, 'post': posts['assoc_prof'],
            'internal_phone': '4003', 'city_phone': '+7 (495) 123-48-03',
            'email': 'popov@university.ru'
        },
        # Старшие преподаватели
        {
            'surname': 'Федорова', 'name': 'Татьяна', 'middle_name': 'Андреевна',
            'academic_degree': None, 'role': role_teacher,
            'subdivision': dept_programming, 'post': posts['senior_lect'],
            'internal_phone': '5001', 'city_phone': '+7 (495) 123-49-01',
            'email': 'fedorova@university.ru'
        },
        {
            'surname': 'Михайлов', 'name': 'Игорь', 'middle_name': 'Петрович',
            'academic_degree': None, 'role': role_teacher,
            'subdivision': dept_networks, 'post': posts['senior_lect'],
            'internal_phone': '5002', 'city_phone': '+7 (495) 123-49-02',
            'email': 'mikhailov@university.ru'
        },
    ]
    
    for emp_data in employees_data:
        employee, created = Employee.objects.get_or_create(
            surname=emp_data['surname'],
            name=emp_data['name'],
            defaults={
                'middle_name': emp_data['middle_name'],
                'academic_degree': emp_data['academic_degree'],
                'role': emp_data['role']
            }
        )
        
        # Создаем контакт
        EmployeeDivision.objects.get_or_create(
            employee=employee,
            subdivision=emp_data['subdivision'],
            post=emp_data['post'],
            defaults={
                'internal_phone': emp_data['internal_phone'],
                'city_phone': emp_data['city_phone'],
                'email': emp_data['email']
            }
        )
    
    print(f"   Создано сотрудников: {Employee.objects.count()}")
    print(f"   Создано контактов: {EmployeeDivision.objects.count()}")
    
    # Создаем типы событий
    print("\n7. Создание типов событий...")
    event_types = [
        TypeEvent.objects.get_or_create(name="Конференция")[0],
        TypeEvent.objects.get_or_create(name="Семинар")[0],
        TypeEvent.objects.get_or_create(name="Лекция")[0],
        TypeEvent.objects.get_or_create(name="Защита диссертации")[0],
    ]
    print(f"   Создано типов событий: {TypeEvent.objects.count()}")
    
    # Создаем события
    print("\n8. Создание событий...")
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    events_data = [
        # Мероприятия на сегодня
        {
            'name': 'Научный семинар кафедры программирования',
            'start': today.replace(hour=10, minute=0),
            'end': today.replace(hour=12, minute=0),
            'type': event_types[1],
            'location': locations[3],
            'organizer': Employee.objects.get(surname='Козлов')
        },
        {
            'name': 'Защита курсовых проектов',
            'start': today.replace(hour=14, minute=0),
            'end': today.replace(hour=16, minute=0),
            'type': event_types[3],
            'location': locations[0],
            'organizer': Employee.objects.get(surname='Иванов')
        },
        {
            'name': 'Встреча с работодателями',
            'start': today.replace(hour=15, minute=0),
            'end': today.replace(hour=17, minute=0),
            'type': event_types[1],
            'location': locations[6],
            'organizer': Employee.objects.get(surname='Смирнова')
        },
        # Будущие мероприятия
        {
            'name': 'Международная конференция по искусственному интеллекту',
            'start': today + timedelta(days=7, hours=9),
            'end': today + timedelta(days=7, hours=18),
            'type': event_types[0],
            'location': locations[0],
            'organizer': Employee.objects.get(surname='Иванов')
        },
        {
            'name': 'Семинар по машинному обучению',
            'start': today + timedelta(days=14, hours=10),
            'end': today + timedelta(days=14, hours=12),
            'type': event_types[1],
            'location': locations[3],
            'organizer': Employee.objects.get(surname='Козлов')
        },
        {
            'name': 'Открытая лекция: Квантовые вычисления',
            'start': today + timedelta(days=21, hours=14),
            'end': today + timedelta(days=21, hours=16),
            'type': event_types[2],
            'location': locations[2],
            'organizer': Employee.objects.get(surname='Сидоров')
        },
    ]
    
    for event_data in events_data:
        Event.objects.get_or_create(
            name=event_data['name'],
            defaults={
                'start_datetime': event_data['start'],
                'end_datetime': event_data['end'],
                'location': event_data['location'],
                'type_event': event_data['type'],
                'organizer': event_data['organizer']
            }
        )
    
    print(f"   Создано событий: {Event.objects.count()}")

if __name__ == '__main__':
    populate()

    # Создаем предметы и расписание
    print("\n9. Создание предметов...")
    from schedule.models import Subject, LessonType, Schedule
    from datetime import time
    
    # Получаем локации заново
    all_locations = list(Location.objects.all()[:6])
    
    subjects = [
        Subject.objects.get_or_create(name="Программирование на Python")[0],
        Subject.objects.get_or_create(name="Базы данных")[0],
        Subject.objects.get_or_create(name="Компьютерные сети")[0],
        Subject.objects.get_or_create(name="Алгоритмы и структуры данных")[0],
        Subject.objects.get_or_create(name="Математический анализ")[0],
        Subject.objects.get_or_create(name="Линейная алгебра")[0],
    ]
    print(f"   Создано предметов: {Subject.objects.count()}")
    
    print("\n10. Создание типов занятий...")
    lesson_types = {
        'lecture': LessonType.objects.get_or_create(name="Лекция")[0],
        'practice': LessonType.objects.get_or_create(name="Практика")[0],
        'lab': LessonType.objects.get_or_create(name="Лабораторная работа")[0],
    }
    print(f"   Создано типов занятий: {LessonType.objects.count()}")
    
    print("\n11. Создание расписания...")
    # Получаем больше локаций
    all_locations = list(Location.objects.all())
    
    schedule_data = [
        # Понедельник - Корпус 2, аудитория 405
        {
            'subject': subjects[0], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Козлов'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 1,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[0], 'lesson_type': lesson_types['lab'],
            'teacher': Employee.objects.get(surname='Лебедев'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 1,
            'start_time': time(10, 45), 'end_time': time(12, 15)
        },
        {
            'subject': subjects[4], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Морозова'),
            'location': Location.objects.get(building="Корпус 3", room="210"), 'weekday': 1,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[3], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Лебедев'),
            'location': Location.objects.get(building="Корпус 1", room="205"), 'weekday': 1,
            'start_time': time(12, 30), 'end_time': time(14, 0)
        },
        # Вторник - Корпус 2, аудитория 405
        {
            'subject': subjects[1], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Волков'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 2,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[2], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Смирнова'),
            'location': Location.objects.get(building="Корпус 2", room="301"), 'weekday': 2,
            'start_time': time(10, 45), 'end_time': time(12, 15)
        },
        {
            'subject': subjects[5], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Попов'),
            'location': Location.objects.get(building="Корпус 3", room="210"), 'weekday': 2,
            'start_time': time(10, 45), 'end_time': time(12, 15)
        },
        # Среда - Корпус 2, аудитория 405
        {
            'subject': subjects[3], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Козлов'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 3,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[5], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Попов'),
            'location': Location.objects.get(building="Корпус 3", room="210"), 'weekday': 3,
            'start_time': time(12, 30), 'end_time': time(14, 0)
        },
        {
            'subject': subjects[2], 'lesson_type': lesson_types['lab'],
            'teacher': Employee.objects.get(surname='Соколова'),
            'location': Location.objects.get(building="Корпус 1", room="301"), 'weekday': 3,
            'start_time': time(14, 15), 'end_time': time(15, 45)
        },
        # Четверг - Корпус 2, аудитория 405
        {
            'subject': subjects[1], 'lesson_type': lesson_types['lab'],
            'teacher': Employee.objects.get(surname='Волков'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 4,
            'start_time': time(10, 45), 'end_time': time(12, 15)
        },
        {
            'subject': subjects[2], 'lesson_type': lesson_types['lecture'],
            'teacher': Employee.objects.get(surname='Соколова'),
            'location': Location.objects.get(building="Корпус 2", room="301"), 'weekday': 4,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[0], 'lesson_type': lesson_types['lab'],
            'teacher': Employee.objects.get(surname='Федорова'),
            'location': Location.objects.get(building="Корпус 3", room="210"), 'weekday': 4,
            'start_time': time(12, 30), 'end_time': time(14, 0)
        },
        # Пятница - Корпус 2, аудитория 405
        {
            'subject': subjects[0], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Федорова'),
            'location': Location.objects.get(building="Корпус 2", room="405"), 'weekday': 5,
            'start_time': time(9, 0), 'end_time': time(10, 30)
        },
        {
            'subject': subjects[4], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Морозова'),
            'location': Location.objects.get(building="Корпус 3", room="210"), 'weekday': 5,
            'start_time': time(10, 45), 'end_time': time(12, 15)
        },
        {
            'subject': subjects[1], 'lesson_type': lesson_types['practice'],
            'teacher': Employee.objects.get(surname='Волков'),
            'location': Location.objects.get(building="Корпус 1", room="205"), 'weekday': 5,
            'start_time': time(14, 15), 'end_time': time(15, 45)
        },
    ]
    
    for sched_data in schedule_data:
        Schedule.objects.get_or_create(
            subject=sched_data['subject'],
            lesson_type=sched_data['lesson_type'],
            teacher=sched_data['teacher'],
            location=sched_data['location'],
            weekday=sched_data['weekday'],
            start_time=sched_data['start_time'],
            defaults={'end_time': sched_data['end_time']}
        )
    
    print(f"   Создано записей расписания: {Schedule.objects.count()}")
    
    print("\n✅ База данных успешно наполнена тестовыми данными!")
    print("\nСтатистика:")
    print(f"   - Ролей: {Role.objects.count()}")
    print(f"   - Типов подразделений: {TypeDivision.objects.count()}")
    print(f"   - Локаций: {Location.objects.count()}")
    print(f"   - Должностей: {Post.objects.count()}")
    print(f"   - Подразделений: {Subdivision.objects.count()}")
    print(f"   - Сотрудников: {Employee.objects.count()}")
    print(f"   - Контактов: {EmployeeDivision.objects.count()}")
    print(f"   - Типов событий: {TypeEvent.objects.count()}")
    print(f"   - Событий: {Event.objects.count()}")
    print(f"   - Предметов: {Subject.objects.count()}")
    print(f"   - Типов занятий: {LessonType.objects.count()}")
    print(f"   - Записей расписания: {Schedule.objects.count()}")
