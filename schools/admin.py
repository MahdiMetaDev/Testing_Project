from django.contrib import admin

from .models import Student


@admin.register(Student)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mark', ]
