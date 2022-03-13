from django.urls import path
from .views import (
    StudentsView,
    StudentAddView,
    StudentView,
    StudentEditView,
    )


urlpatterns = [
    path('students/', StudentsView.as_view(), name='students'),
    path('students/add/', StudentAddView.as_view(), name='student_add'),
    path('students/<int:pk>/', StudentView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', StudentEditView.as_view(), name='student_edit'),

]