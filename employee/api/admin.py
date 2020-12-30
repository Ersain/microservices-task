from django.contrib import admin

from .models import Employee, Department, PositionIds

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(PositionIds)
