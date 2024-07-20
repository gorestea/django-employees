from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (DepartmentViewSet, EmployeeViewSet, get_sub_departments, get_department_employees,
                    get_employee_details)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('departments/<int:department_id>/sub_departments/', get_sub_departments, name='sub-departments'),
    path('departments/<int:department_id>/employees/', get_department_employees, name='department-employees'),
    path('employees/<int:employee_id>/', get_employee_details, name='employee-details'),
]
