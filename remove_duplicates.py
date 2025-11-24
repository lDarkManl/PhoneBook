"""
Скрипт для удаления дубликатов сотрудников и подразделений
Запуск: python remove_duplicates.py
"""
import os
import django
import sys

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PhoneBook.settings')
django.setup()

from employees.models import Employee
from structure.models import Subdivision
from contacts.models import EmployeeDivision

def remove_duplicates():
    print("Начинаем удаление дубликатов...")
    
    # 1. Удаляем дублирующиеся подразделения
    print("\n1. Проверка дублирующихся подразделений...")
    subdivisions = Subdivision.objects.all().order_by('id')
    seen_names = {}
    duplicates_count = 0
    
    for subdivision in subdivisions:
        if subdivision.name in seen_names:
            original = seen_names[subdivision.name]
            print(f"   Найден дубликат: {subdivision.name} (ID: {subdivision.id}, оригинал ID: {original.id})")
            
            # Переносим все связанные контакты на оригинальное подразделение
            contacts = EmployeeDivision.objects.filter(subdivision=subdivision)
            for contact in contacts:
                # Проверяем, нет ли уже такого контакта у оригинального подразделения
                existing = EmployeeDivision.objects.filter(
                    employee=contact.employee,
                    subdivision=original,
                    post=contact.post
                ).first()
                
                if existing:
                    print(f"      Удаляем дублирующийся контакт: {contact.employee.surname}")
                    contact.delete()
                else:
                    print(f"      Переносим контакт: {contact.employee.surname}")
                    contact.subdivision = original
                    contact.save()
            
            # Переносим дочерние подразделения
            children = Subdivision.objects.filter(parent=subdivision)
            for child in children:
                print(f"      Переносим дочернее подразделение: {child.name}")
                child.parent = original
                child.save()
            
            # Теперь можно удалить дубликат
            subdivision.delete()
            duplicates_count += 1
        else:
            seen_names[subdivision.name] = subdivision
    
    print(f"   Удалено дублирующихся подразделений: {duplicates_count}")
    print(f"   Осталось подразделений: {Subdivision.objects.count()}")
    
    # 2. Удаляем дублирующиеся записи сотрудников
    print("\n2. Проверка дублирующихся сотрудников...")
    employees = Employee.objects.all()
    seen_employees = {}
    duplicates_count = 0
    
    for employee in employees:
        key = f"{employee.surname}_{employee.name}_{employee.middle_name}"
        if key in seen_employees:
            print(f"   Удаляем дубликат: {employee.surname} {employee.name} (ID: {employee.id})")
            employee.delete()
            duplicates_count += 1
        else:
            seen_employees[key] = employee
    
    print(f"   Удалено дублирующихся сотрудников: {duplicates_count}")
    print(f"   Осталось сотрудников: {Employee.objects.count()}")
    
    # 3. Удаляем дублирующиеся контакты (один сотрудник в одном подразделении)
    print("\n3. Проверка дублирующихся контактов...")
    contacts = EmployeeDivision.objects.all()
    seen_contacts = {}
    duplicates_count = 0
    
    for contact in contacts:
        key = f"{contact.employee.id}_{contact.subdivision.id}_{contact.post.id}"
        if key in seen_contacts:
            print(f"   Удаляем дубликат контакта: {contact.employee.surname} в {contact.subdivision.name} (ID: {contact.id})")
            contact.delete()
            duplicates_count += 1
        else:
            seen_contacts[key] = contact
    
    print(f"   Удалено дублирующихся контактов: {duplicates_count}")
    print(f"   Осталось контактов: {EmployeeDivision.objects.count()}")
    
    print("\n✅ Удаление дубликатов завершено!")
    print("\nИтоговая статистика:")
    print(f"   - Подразделений: {Subdivision.objects.count()}")
    print(f"   - Сотрудников: {Employee.objects.count()}")
    print(f"   - Контактов: {EmployeeDivision.objects.count()}")

if __name__ == '__main__':
    remove_duplicates()
