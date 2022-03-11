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
    sales_manager = models.ManyToManyField(SalesManager, related_name='student')
    notes = models.TextField(blank=True)


    def has_classes_left(self):
        return self.classes_left < 10

    def get_parents(self):
        return self.parent.all()

    def get_sales_managers(self):
        return self.sales_manager.all()
