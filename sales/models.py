"""Models for the sales app."""
from django.db import models
from profiles.models import SalesManager, Parent
from students.models import Student


class Sales(models.Model):
    """Sales model"""
    sold_by = models.ForeignKey(SalesManager, on_delete=models.CASCADE, related_name='sold')
    sold_to = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='bought')
    # add_to_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='added_to')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
