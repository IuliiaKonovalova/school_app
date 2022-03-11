from django.db import models
from profiles.models import Parent
from sales.models import SalesManager

# Create your models here.

class Student(models.Model):
    """Student model"""
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    parent = models.ManyToManyField(Parent, related_name='child')
    birthday = models.DateField()
    address = models.CharField(max_length=100, blank=True, null=True)
    enrolled = models.DateTimeField(auto_now_add=True)
    classes_left = models.IntegerField()
    # It's a foreign key to the sales manager for sorting kids by a manager assigned to them
    sales_manager = models.ManyToManyField(SalesManager, related_name='student')
    notes = models.TextField(blank=True)

    # add method to check weather the student has less than 10 classes left
    def has_classes_left(self):
        return self.classes_left < 10
