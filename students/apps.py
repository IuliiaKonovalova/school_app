"""Apps for the students app."""
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    """students config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
