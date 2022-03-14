"""Apps for the sales app."""
from django.apps import AppConfig


class SalesConfig(AppConfig):
    """sales config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
