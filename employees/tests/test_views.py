
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from employees.models import Department, Employee
from datetime import date


class DepartmentViewSetTest(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Test Department")

    def test_get_departments(self):
        url = reverse('department-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], "Test Department")


class EmployeeViewSetTest(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Test Department")
        self.employee = Employee.objects.create(
            full_name="John Doe",
            position="Developer",
            hire_date=date.today(),
            salary=50000,
            department=self.department
        )

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['full_name'], "John Doe")
        self.assertEqual(response.data[0]['position'], "Developer")
