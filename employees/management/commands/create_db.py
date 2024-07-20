import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from employees.models import Department, Employee

class Command(BaseCommand):
    help = 'Заполнение базы данных начальными данными'

    def handle(self, *args, **kwargs):
        # Создание 25 подразделений с иерархией до 5 уровней
        departments = []
        for i in range(1, 26):
            parent = random.choice(departments) if departments else None
            department = Department.objects.create(name=f'Department {i}', parent=parent)
            departments.append(department)

        # Создание 50,000 сотрудников
        positions = ['Manager', 'Developer', 'Designer', 'Tester', 'Analyst']
        for i in range(50000):
            department = random.choice(departments)
            hire_date = date.today() - timedelta(days=random.randint(0, 3650))
            salary = round(random.uniform(30000, 150000), 2)
            Employee.objects.create(
                full_name=f'Employee {i + 1}',
                position=random.choice(positions),
                hire_date=hire_date,
                salary=salary,
                department=department
            )
