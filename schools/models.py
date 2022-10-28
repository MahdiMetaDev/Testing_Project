from django.db import models


class Student(models.Model):

    MARK_CHOICES = [
        ('1', 'Good'),
        ('2', 'Very Good'),
    ]
    DEFAULT_DISPLAY = [
        (None, 'Your String For Display'),
    ]
    first_name = models.CharField(max_length=100, choices=DEFAULT_DISPLAY)
    last_name = models.CharField(max_length=100, choices=DEFAULT_DISPLAY)
    mark = models.CharField(max_length=50, choices=MARK_CHOICES)
