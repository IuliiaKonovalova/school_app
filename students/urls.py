from django.urls import path
from .views import (
    StudentsView,
    StudentAddView,
    )


urlpatterns = [
    path('<slug:phone>/', StudentsView.as_view(), name='students'),
    path('<slug:phone>/search/', StudentAddView.as_view(), name='student_add'),

]