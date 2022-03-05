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
    """Receptionist model"""
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    lessons_created = models.ManyToManyField(Lesson, related_name='receptionists')



class SalesManager(models.Model):
    """Sales model"""
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    lessons_sold = models.ManyToManyField(Sales, related_name='sales_manager')


class Parent(models.Model):
    """Parent model"""
    # Gaurdian's relation to the student
    GUARDIAN_RELATION = (
        (1, 'father'),
        (2, 'mother'),
        (3, 'grandfather'),
        (4, 'grandmother'),
        (5, 'other'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    relation = models.IntegerField(choices=GUARDIAN_RELATION, default=5)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)


class Student(models.Model):
    """Student model"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL)
    birthday = models.DateField()
    enrolled = models.DateTimeField(auto_now_add=True)
    classes_bought = models.IntegerField()
    subjects = models.ManyToManyField(Subject, related_name='students')
    lessons_attended = models.ManyToManyField(Lesson, related_name='students')
    # It's a foreign key to the sales manager for sorting kids by a manager assigned to them
    sales_manager = models.ForeignKey(Sales, on_delete=models.SET_NULL)
