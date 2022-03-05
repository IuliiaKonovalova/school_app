from django.db import models
from subjects.models import Subject
from profiles.models import Teacher, Student

class Lesson(models.Model):
    """Lesson model"""
    date = models.DateTimeField()
    time = models.DateField()
    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, related_name='lessons')
    students = models.ManyToManyField(Student, related_name='lessons')