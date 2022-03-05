from django.db import models
from django.contrib.auth.models import AbstractUser
from subjects.models import Subject
from lessons.models import Lesson
from sales.models import Sales


# Roles to assign to users
ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (3, 'sales'),
        (4, 'receptionist'),
        (5, 'parent'),
        (6, 'potential user'),
)

class CustomUser(AbstractUser):
    """Custom user model"""
    username = models.CharField(max_length=50, blank=False, null=True, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    role = models.IntegerField(choices=ROLES, default=6)

    def __str__(self):
        return self.email

    # Add meta class to define admin interface
    class Meta:
        """Meta class"""
        ordering = ['email']


class Teacher(models.Model):
    """Teacher model"""
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    lessons = models.ManyToManyField(Lesson, related_name='teachers')


class Receptionist(models.Model):
    """
    Receptionist model
    """
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    lessons_created = models.ManyToManyField(Lesson, related_name='receptionists')