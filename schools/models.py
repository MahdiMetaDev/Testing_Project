from django.db import models


class Student(models.Model):

    MARK_CHOICES = [
        (None, 'Your String For Display'),
        ('1', 'Bad'),
        ('2', 'Good'),
        ('3', 'Very Good'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mark = models.CharField(max_length=50, choices=MARK_CHOICES)

    def __str__(self):
        return self.first_name
