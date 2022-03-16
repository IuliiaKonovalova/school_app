"""Urls for the lessons app."""
from django.urls import path
from .views import LessonsView, LessonAddView, LessonEditView


urlpatterns = [
    path('', LessonsView.as_view(), name='lessons_list'),
    path('add/', LessonAddView.as_view(), name='lesson_add'),
    path('<int:pk>/edit/', LessonEditView.as_view(), name='lesson_edit'),
]
