"""Tests for the forms of the lessons app."""
from django.test import TestCase
from lessons.forms import LessonForm
from profiles.models import (
    CustomUser,
    Teacher,
    Receptionist,
    SalesManager,
    Parent
)
from students.models import Student
from lessons.models import TIME_PERIODS, SUBJECTS


class TestLessonForm(TestCase):
    """Test the LessonForm."""
    def setUp(self):
        """Set up the test."""
        # create users
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@potential.com',
            password='Testuser123',
            first_name='test',
            last_name='user',
            phone='1234567890',
            role = CustomUser.ROLES[5][0],
        )
        self.user_boss = CustomUser.objects.create(
            username='boss',
            email='boss@gmail.com',
            password='boss',
            first_name='boss',
            last_name='boss',
            phone='1234567890',
            role = CustomUser.ROLES[0][0],
        )
        self.user_teacher = CustomUser.objects.create(
            username='teacher',
            email = 'teacher@gmail.com',
            password = 'teacher',
            first_name = 'teacher',
            last_name = 'teacher',
            phone = '1234567890',
            role = CustomUser.ROLES[1][0],
        )
        self.user_sales_manager = CustomUser.objects.create(
            username='sales_manager',
            email = 'salesmanager@gmail.com',
            password = 'salesmanager',
            first_name = 'salesmanager',
            last_name = 'salesmanager',
            phone = '1234567890',
            role = CustomUser.ROLES[2][0],
        )
        self.user_receptionist = CustomUser.objects.create(
            username='receptionist',
            email = 'receptionist@gmail.com',
            password = 'receptionist',
            first_name = 'receptionist',
            last_name = 'receptionist',
            phone = '1234567890',
            role = CustomUser.ROLES[3][0],
        )
        self.user_parent = CustomUser.objects.create(
            username='parent',
            email = 'parent@gmail.com',
            password = 'parent',
            first_name = 'parent',
            last_name = 'parent',
            phone = '1234567890',
            role = CustomUser.ROLES[4][0],
        )
        self.potential = CustomUser.objects.create(
            username='potential',
            email = 'potential@gmail.com',
            password = 'potential',
            first_name = 'potential',
            last_name = 'potential',
            phone = '1234567890',
            role = CustomUser.ROLES[5][0],
        )
        self.teacher_member = Teacher.objects.create(
            user = CustomUser.objects.get(id=self.user_teacher.id),
        )
        self.receptionist_member = Receptionist.objects.create(
            user = CustomUser.objects.get(id=self.user_receptionist.id),
        )
        self.parent_member = Parent.objects.create(
            user = CustomUser.objects.get(id = self.user_parent.id),
            relation = Parent.GUARDIAN_RELATION[4][0],
        )
        self.sales_manager_member = SalesManager.objects.create(
            id = 1,
            user = CustomUser.objects.get(id = self.user_sales_manager.id),
            total_sold = 0,
        )
        sales_manager_pk = SalesManager.objects.get(pk=1)
        # create student
        self.student = Student.objects.create(
            first_name = 'student1FirstName',
            last_name = 'student1Surname',
            birthday = '2000-01-01',
            address = 'student1Address',
            enrolled = '01/01/2000',
            classes_left = 50,
            notes = 'student1Notes',
        )

        self.student2 = Student.objects.create(
            first_name = 'student1FirstName',
            last_name = 'student1Surname',
            birthday = '2000-01-01',
            address = 'student1Address',
            enrolled = '01/01/2000',
            classes_left = 50,
            notes = 'student1Notes',
        )
        self.student.parent.add(Parent.objects.get(id=1))
        self.student.sales_manager.add(sales_manager_pk)

    def test_form_has_fields(self):
        """Test the form has the correct fields."""
        form = LessonForm()
        expected = ['date', 'time', 'subject', 'teachers', 'students']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_form_date_field_label(self):
        """Test the label of the date field."""
        form = LessonForm()
        self.assertTrue(form.fields['date'].label == 'Date')
        self.assertTrue(form.fields['date'].widget.attrs['class'] == 'form-control')
        self.assertTrue(form.fields['time'].label == 'Time')
        self.assertTrue(form.fields['time'].widget.attrs['class'] == 'form-control')
        self.assertTrue(form.fields['subject'].label == 'Subject')
        self.assertTrue(form.fields['subject'].widget.attrs['class'] == 'form-control')
        self.assertTrue(form.fields['teachers'].label == 'Teachers')
        self.assertTrue(form.fields['teachers'].widget.attrs['class'] == 'form-control')
        self.assertTrue(form.fields['students'].label == 'Students')
        self.assertTrue(form.fields['students'].widget.attrs['class'] == 'form-control')

    def test_lesson_form_is_valid(self):
        """Test the form is valid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_lesson_form_no_data(self):
        """Test the form is invalid."""
        form = LessonForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_lesson_form_invalid_date(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-12',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_time(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': '12:00',
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_subject(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': 'japanese',
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_no_date(self):
        """Test the form is invalid."""
        form = LessonForm({
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_no_time(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_no_subject(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': TIME_PERIODS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_no_teacher(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [],
            'students': [Student.objects.get(id=1)],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_lesson_form_invalid_no_student(self):
        """Test the form is invalid."""
        form = LessonForm({
            'date': '2019-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [Teacher.objects.get(id=1)],
            'students': [],
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
