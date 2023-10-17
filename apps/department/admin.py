from django.contrib import admin

from apps.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ...