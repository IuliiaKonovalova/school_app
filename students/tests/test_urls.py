"""Tests for the students app's urls."""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from students.views import (
    StudentsView,
    StudentAddView,
    StudentView,
    StudentEditView,
    StudentDeleteView,
    )


class TestUrls(SimpleTestCase):
    """Test the urls for the students app."""

    def test_students_url_resolves(self):
        """Test the students url resolves."""
        url = reverse('students')
        self.assertEquals(resolve(url).func.view_class, StudentsView)

    def test_student_add_url_resolves(self):
        """Test the student add url resolves."""
        url = reverse('student_add')
        self.assertEquals(resolve(url).func.view_class, StudentAddView)

    def test_student_detail_url_resolves(self):
        """Test the student detail url resolves."""
        url = reverse('student_detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, StudentView)

    def test_student_edit_url_resolves(self):
        """Test the student edit url resolves."""
        url = reverse('student_edit', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, StudentEditView)

    def test_student_delete_url_resolves(self):
        """Test the student delete url resolves."""
        url = reverse('student_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, StudentDeleteView)
