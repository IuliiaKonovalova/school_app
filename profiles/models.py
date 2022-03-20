"""Models for profiles app."""
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
    username = models.CharField(
        max_length=50, blank=False,
        null=True,
        unique=True
    )
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    role = models.IntegerField(choices=ROLES, default=5)

    def __str__(self):
        return str(self.username)
    class Meta:
        """Meta class"""
        ordering = ['email']


class Teacher(models.Model):
    """Teacher model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Receptionist(models.Model):
    """Receptionist model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class SalesManager(models.Model):
    """Sales model"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


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

    def get_relation(self):
        return dict(self.GUARDIAN_RELATION)[self.relation]
        
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

