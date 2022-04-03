"""Test for forms in the lessons app"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lessons.views import (
    LessonsView,
    LessonAddView,
    LessonEditView,
    LessonDeleteView,
    LessonDetailView,
    TeacherScheduleView
)


class TestUrls(SimpleTestCase):
    """Test the urls for the lessons app."""
    def test_lessons_url(self):
        """Test the lessons url."""
        url = reverse('lessons_list')
        self.assertEqual(resolve(url).func.view_class, LessonsView)

    def test_lesson_add_url(self):
        """Test the lesson_add url."""
        url = reverse('lesson_add')
        self.assertEqual(resolve(url).func.view_class, LessonAddView)

    def test_lesson_edit_url(self):
        """Test the lesson_edit url."""
        url = reverse('lesson_edit', args=['1'])
        self.assertEqual(resolve(url).func.view_class, LessonEditView)

    def test_lesson_delete_url(self):
        """Test the lesson_delete url."""
        url = reverse('lesson_delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, LessonDeleteView)

    def test_lesson_detail_url(self):
        """Test the lesson_detail url."""
        url = reverse('lesson_detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, LessonDetailView)

    def test_teacher_schedule_url(self):
        """Test the teacher_schedule url."""
        url = reverse('teacher_schedule')
        self.assertEqual(resolve(url).func.view_class, TeacherScheduleView)
