"""Urls for the lessons app."""
from django.urls import path
from .views import LessonsView, LessonAddView, LessonEditView, LessonDeleteView, LessonDetailView, TeacherScheduleView


urlpatterns = [
    path('', LessonsView.as_view(), name='lessons_list'),
    path('add/', LessonAddView.as_view(), name='lesson_add'),
    path('<int:pk>/edit/', LessonEditView.as_view(), name='lesson_edit'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('teacher_schedule/', TeacherScheduleView.as_view(), name='teacher_schedule'),
]
