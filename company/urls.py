from django.contrib import admin
from django.urls import path, include
from employees.views import department_tree

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('', department_tree, name='home'),
    # path('__debug__/', include('debug_toolbar.urls')),
]
