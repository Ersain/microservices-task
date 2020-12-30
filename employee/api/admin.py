from django.contrib import admin

from .models import Employee, Department, PositionId

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(PositionId)
