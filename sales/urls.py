"""Urls for the sales app."""
from django.urls import path
from .views import SalesView, sales_form, edit_sales, delete_sales


urlpatterns = [
    path('sales/', SalesView.as_view(), name='sales_list'),
    path('sales/add/', sales_form, name='sales_form'),
    path('sales/edit/<int:pk>/', edit_sales, name='edit_sales'),
    path('sales/delete/<int:pk>/', delete_sales, name='delete_sales'),
]
