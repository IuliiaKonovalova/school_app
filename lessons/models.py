"""Models for the lessons app"""
from django.db import models
from subjects.models import Subject
from profiles.models import Teacher
from students.models import Student


TIMEPERIODS = (
        (0, '9:00-9:45'),
        (1, '10:00-10:45'),
        (2, '11:00-11:45'),
        (3, '14:00-14:45'),
        (4, '15:00-15:45'),
        (5, '16:00-16:45'),
        (6, '17:00-17:45'),
        (7, '18:00-18:45'),
)


class Lesson(models.Model):
    """Lesson model"""
    date = models.DateTimeField()
    time_period = models.IntegerField(choices=TIMEPERIODS, default=0)
    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, related_name='lessons')
    students = models.ManyToManyField(Student, related_name='lessons')
