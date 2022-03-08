from django.db import models
from django.contrib.auth.models import AbstractUser


# Roles to assign to users
ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (2, 'sales'),
        (3, 'receptionist'),
        (4, 'parent'),
        (5, 'potential user'),
)

class CustomUser(AbstractUser):
    """Custom user model"""
    username = models.CharField(max_length=50, blank=False, null=True, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True, blank=False)
    role = models.IntegerField(choices=ROLES, default=5)

    def __str__(self):
        return self.email

    # Add meta class to define admin interface
    class Meta:
        """Meta class"""
        ordering = ['email']


class Teacher(models.Model):
    """Teacher model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Receptionist(models.Model):
    """Receptionist model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class SalesManager(models.Model):
    """Sales model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    relation = models.IntegerField(choices=GUARDIAN_RELATION, default=5)
    address = models.CharField(max_length=100, default='', blank=True)
