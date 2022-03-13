"""Models for the students app."""
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
        """Check if student has classes left"""
        return self.classes_left < 10

    def get_parents(self):
        """Get all parents of the student"""
        return self.parent.all()

    def get_sales_managers(self):
        """Get all sales managers of the student"""
        return self.sales_manager.all()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # Add ordering by date of last enrolment
    class Meta:
        db_table = 'students'
        ordering = ['-enrolled']
