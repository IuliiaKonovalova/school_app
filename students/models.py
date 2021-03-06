"""Models for the students app."""
from django.db import models
from profiles.models import Parent
from sales.models import SalesManager


class Student(models.Model):
    """Student model"""
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    parent = models.ManyToManyField(Parent, related_name='child')
    birthday = models.DateField()
    address = models.CharField(max_length=100, blank=True, null=True)
    enrolled = models.DateTimeField(auto_now_add=True)
    classes_left = models.IntegerField(default=0, blank=True, null=True)
    sales_manager = models.ManyToManyField(
        SalesManager,
        related_name='student'
    )
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

    def get_parent_usernames(self):
        """Get all parents of the student"""
        return [parent.user.username for parent in self.get_parents()]

    def __str__(self):
        """Return string representation of student."""
        return self.first_name + ' ' + self.last_name

    class Meta:
        """Meta class"""
        db_table = 'students'
        ordering = ['-enrolled']
