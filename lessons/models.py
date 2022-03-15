"""Models for the lessons app"""
from django.db import models
from profiles.models import Teacher
from students.models import Student


TIME_PERIODS = (
        (0, '9:00-9:45'),
        (1, '10:00-10:45'),
        (2, '11:00-11:45'),
        (3, '14:00-14:45'),
        (4, '15:00-15:45'),
        (5, '16:00-16:45'),
        (6, '17:00-17:45'),
        (7, '18:00-18:45'),
)

SUBJECT = (
        (1, 'art'),
        (2, 'math'),
        (3, 'casa'),
        (4, 'chinese'),
        (5, 'toddlers'),
        (6, 'music'),
        (7, 'english'),
        (8, 'sport'),
        (9, 'cooking'),
        (10, 'infants'),
    )

class Lesson(models.Model):
    """Lesson model"""
    date = models.DateTimeField()
    time_period = models.IntegerField(choices=TIME_PERIODS, default=0)
    subject = models.IntegerField(choices=SUBJECT, default=0)
    teachers = models.ManyToManyField(Teacher, related_name='lessons')
    students = models.ManyToManyField(Student, related_name='lessons')
