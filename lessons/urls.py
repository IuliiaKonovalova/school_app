"""Urls for the lessons app."""
from django.urls import path
from .views import LessonAddView


urlpatterns = [
    path('add/', LessonAddView.as_view(), name='lesson_add'),
]