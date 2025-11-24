# Инструкции по настройке нового дизайна

## Что изменилось

### 1. Главная страница
- Поиск преподавателей с фильтрами (ФИО, должность, подразделение, аудитория)
- Кнопка экспорта в Excel
- Блок с деканами факультетов
- Блок с ближайшими мероприятиями

### 2. Базовый шаблон (base.html)
- Новая шапка с кнопками: Домой, Сотрудники, Подразделения, Аудитории
- Подвал с годом 2025
- Улучшенный дизайн с градиентами

### 3. Модель Event
- Добавлено поле `image` для фото мероприятий

## Шаги для запуска

### 1. Установите необходимые пакеты
```bash
pip install openpyxl Pillow
```

### 2. Создайте миграции для модели Event
```bash
python manage.py makemigrations events
python manage.py migrate
```

### 3. Создайте тестовые данные (опционально)

#### Создайте деканов
В Django admin или через shell создайте сотрудников с должностью "Декан":
```python
python manage.py shell

from employees.models import Employee
from accounts.models import Role
from positions.models import Post
from structure.models import Subdivision, Location, TypeDivision
from contacts.models import EmployeeDivision

# Создайте должность "Декан"
dean_post, _ = Post.objects.get_or_create(name="Декан факультета")

# Создайте сотрудника-декана
role = Role.objects.first()
employee = Employee.objects.create(
    surname="Иванов",
    name="Иван",
    middle_name="Иванович",
    role=role
)

# Создайте подразделение (факультет)
type_div, _ = TypeDivision.objects.get_or_create(name="Факультет")
location, _ = Location.objects.get_or_create(building="Корпус 1", room="101")
subdivision = Subdivision.objects.create(
    name="Факультет информационных технологий",
    id_type_division=type_div,
    id_location=location
)

# Создайте контакт декана
EmployeeDivision.objects.create(
    employee=employee,
    subdivision=subdivision,
    post=dean_post,
    internal_phone="1234",
    city_phone="+7 (123) 456-78-90",
    email="dean@university.ru"
)
```

#### Создайте мероприятия
```python
from events.models import Event, TypeEvent
from datetime import datetime, timedelta

# Создайте тип мероприятия
event_type, _ = TypeEvent.objects.get_or_create(name="Конференция")

# Создайте мероприятие
Event.objects.create(
    name="Научная конференция 2025",
    start_datetime=datetime.now() + timedelta(days=7),
    end_datetime=datetime.now() + timedelta(days=8),
    location=location,
    type_event=event_type,
    organizer=employee
)
```

### 4. Запустите сервер
```bash
python manage.py runserver
```

### 5. Откройте в браузере
http://127.0.0.1:8000/

## Функционал главной страницы

### Поиск преподавателей
- Быстрый поиск по ФИО в верхней строке
- Расширенные фильтры (кнопка "Фильтры"):
  - ФИО
  - Должность
  - Подразделение
  - Аудитория

### Экспорт в Excel
- Кнопка "Экспорт в Excel" экспортирует всех сотрудников с контактами
- Файл содержит: ФИО, Должность, Подразделение, Аудитория, Телефоны, Email

### Деканы факультетов
- Автоматически отображаются все сотрудники с должностью, содержащей "декан"
- Показывается: ФИО, должность, подразделение, аудитория, телефоны, email

### Ближайшие мероприятия
- Отображаются 6 ближайших мероприятий
- Сортировка по дате начала
- Показывается: фото (если есть), название, дата, место, организатор

## Следующие шаги

Вы упомянули, что нужно сделать еще страницы:
1. ✅ Главная (готова)
2. Сотрудники (нужно доработать?)
3. Подразделения (нужно доработать?)
4. Дерево подразделений (новая страница)
5. Аудитории (новая страница)

Напишите, что делать дальше!
