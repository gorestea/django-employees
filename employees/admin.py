from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Department, Employee


admin.site.register(Department, DraggableMPTTAdmin)
admin.site.register(Employee)
