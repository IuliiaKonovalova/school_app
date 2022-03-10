"""Urls for the sales app."""
from django.urls import path
from .views import SalesView, sales_form


urlpatterns = [
    path('sales/', SalesView.as_view(), name='sales_list'),

]
