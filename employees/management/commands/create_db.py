import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from employees.models import Department, Employee

class Command(BaseCommand):
    help = 'Заполнение базы данных начальными данными'

    def handle(self, *args, **kwargs):
        departments = []
        for i in range(1, 26):
            parent = random.choice(departments) if departments else None
            department = Department.objects.create(name=f'Отдел №{i}', parent=parent)
            departments.append(department)

        positions = ['Менеджер', 'Разработчик', 'Дизайнер', 'Тестировщик', 'Аналитик']
        for i in range(50000):
            department = random.choice(departments)
            hire_date = date.today() - timedelta(days=random.randint(0, 3650))
            salary = round(random.uniform(30000, 150000), 2)
            Employee.objects.create(
                full_name=f'Сотрудник {i + 1}',
                position=random.choice(positions),
                hire_date=hire_date,
                salary=salary,
                department=department
            )
