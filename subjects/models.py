"""Models for the subjects app."""
from django.db import models

class Subject(models.Model):
    """Subject model"""
    SUBJECT = (
        (1, 'art'),
        (2, 'math'),
        (3, 'casa'),
        (4, 'chinese'),
        (5, 'toddlers'),
        (6, 'music'),
        (7, 'english'),
        (8, 'sport'),
        (5, 'cooking'),
        (5, 'infants'),
    )
    subject = models.IntegerField(choices=SUBJECT, default=3)
