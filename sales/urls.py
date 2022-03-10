"""Urls for the sales app."""
from django.urls import path
from .views import SalesView, sales_form


urlpatterns = [
    path('<username>/', SalesView.as_view(), name='sales_list'),
    path('<username>/form/', sales_form, name='sales_form'),
]
