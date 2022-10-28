from django.urls import path

from . import views

urlpatterns = [
    path('', views.students_list_view, name='list-view'),
]
