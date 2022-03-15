"""Urls for the lessons app."""
from django.urls import path
from .views import LessonsView, LessonAddView


urlpatterns = [
    path('', LessonsView.as_view(), name='lessons_list'),
    path('add/', LessonAddView.as_view(), name='lesson_add'),
]