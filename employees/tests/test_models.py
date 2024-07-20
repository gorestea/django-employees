from django.test import TestCase
from employees.models import Department, Employee
from datetime import date


class DepartmentModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Test Department")

    def test_department_creation(self):
        self.assertEqual(self.department.name, "Test Department")


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Test Department")
        self.employee = Employee.objects.create(
            full_name="John Doe",
            position="Developer",
            hire_date=date.today(),
            salary=50000,
            department=self.department
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.full_name, "John Doe")
        self.assertEqual(self.employee.position, "Developer")
        self.assertEqual(self.employee.salary, 50000)
        self.assertEqual(self.employee.department.name, "Test Department")
