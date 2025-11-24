# PhoneBook Frontend

## Что было создано

### Templates (HTML + Bootstrap 5)
- `base.html` - базовый шаблон с навигацией
- `home.html` - главная страница с статистикой
- `employee_list.html`, `employee_detail.html`, `employee_form.html`, `employee_confirm_delete.html`
- `contact_list.html`, `contact_form.html`, `contact_confirm_delete.html`
- `event_list.html`, `event_detail.html`, `event_form.html`, `event_confirm_delete.html`
- `subdivision_list.html`, `subdivision_detail.html`, `subdivision_form.html`, `subdivision_confirm_delete.html`
- `search_results.html` - результаты поиска

### Views (Django Class-Based Views)
Добавлены веб-интерфейсы для всех приложений:
- **employees**: ListView, DetailView, CreateView, UpdateView, DeleteView
- **contacts**: ListView, CreateView, UpdateView, DeleteView
- **events**: ListView, DetailView, CreateView, UpdateView, DeleteView
- **structure**: ListView, DetailView, CreateView, UpdateView, DeleteView
- **PhoneBook**: home, search

### Forms (Django Forms)
- `employees/forms.py` - EmployeeForm
- `contacts/forms.py` - EmployeeDivisionForm
- `events/forms.py` - EventForm
- `structure/forms.py` - SubdivisionForm

### URLs
Настроены маршруты для всех приложений:
- `/` - главная страница
- `/employees/` - сотрудники
- `/contacts/` - контакты
- `/events/` - события
- `/subdivisions/` - подразделения
- `/search/` - поиск
- `/api/` - REST API (существующий)

## Как запустить

1. Убедитесь, что база данных настроена и миграции применены:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Создайте суперпользователя (если еще не создан):
```bash
python manage.py createsuperuser
```

3. Запустите сервер:
```bash
python manage.py runserver
```

4. Откройте браузер:
- Главная страница: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/

## Функционал

### Главная страница
- Статистика по всем разделам
- Быстрый поиск
- Навигация по разделам

### Сотрудники
- Список с поиском по ФИО
- Детальная информация о сотруднике
- Добавление/редактирование/удаление
- Просмотр контактов сотрудника

### Контакты
- Список с поиском и фильтрацией по подразделениям
- Добавление/редактирование/удаление
- Отображение телефонов и email

### События
- Список событий с карточками
- Детальная информация
- Добавление/редактирование/удаление
- Отображение организатора и места проведения

### Подразделения
- Список подразделений
- Детальная информация с сотрудниками
- Добавление/редактирование/удаление

## Технологии
- Django 5.2.7
- Bootstrap 5.3.0
- Bootstrap Icons 1.11.0
- HTML5, CSS3
