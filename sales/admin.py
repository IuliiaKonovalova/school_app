"""Admin for the sales app"""
from django.contrib import admin
from .models import Sales


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    """Sales admin."""
    list_display = ('id', 'sold_by', 'sold_to', 'amount', 'date')
    search_fields = ('sold_by', 'sold_to', 'amount', 'date')
