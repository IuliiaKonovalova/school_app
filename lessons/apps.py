"""Apps for the home app."""
from django.apps import AppConfig


class LessonsConfig(AppConfig):
    """lessons config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lessons'
