from django.db import models
from profiles.models import Parent
from sales.models import SalesManager

# Create your models here.

class Student(models.Model):
    """Student model"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    birthday = models.DateField()
    enrolled = models.DateTimeField(auto_now_add=True)
    classes_left = models.IntegerField()
    # It's a foreign key to the sales manager for sorting kids by a manager assigned to them
    sales_manager = models.ForeignKey(SalesManager, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)