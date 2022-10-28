from django.shortcuts import render

from .models import Student


def students_list_view(request):
    students = Student.objects.all()
    render(request, 'schools/students_list.html', context={'students': students})
