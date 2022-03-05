from django.db import models
from django.contrib.auth.models import AbstractUser


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
        ordering = ['email']


class Teacher(models.Model):
    """Teacher model"""
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField(CustomUser, related_name='teachers')
    lessons = models.ManyToManyField(CustomUser, related_name='teachers')