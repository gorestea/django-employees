from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def department_tree(request):
    root_department = Department.objects.filter(parent=None).first()
    return render(request, 'employees/tree.html', {'department': root_department})

@api_view(['GET'])
def get_sub_departments(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    sub_departments = department.get_children()
    serializer = DepartmentSerializer(sub_departments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_department_employees(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    employees = department.employees.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)