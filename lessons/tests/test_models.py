"""Test cases for the lessons app."""
from django.test import TestCase
from lessons.models import Lesson, TIME_PERIODS, SUBJECTS
from profiles.models import (
    CustomUser,
    Teacher,
    Receptionist,
    SalesManager,
    Parent
)
from students.models import Student


class TestModels(TestCase):
    """Test the models for the lessons app."""
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
            role=CustomUser.ROLES[5][0],
        )
        self.user_boss = CustomUser.objects.create(
            username='boss',
            email='boss@gmail.com',
            password='boss',
            first_name='boss',
            last_name='boss',
            phone='1234567890',
            role=CustomUser.ROLES[0][0],
        )
        self.user_teacher = CustomUser.objects.create(
            username='teacher',
            email='teacher@gmail.com',
            password='teacher',
            first_name='teacher',
            last_name='teacher',
            phone='1234567890',
            role=CustomUser.ROLES[1][0],
        )
        self.user_sales_manager = CustomUser.objects.create(
            username='sales_manager',
            email='salesmanager@gmail.com',
            password='salesmanager',
            first_name='salesmanager',
            last_name='salesmanager',
            phone='1234567890',
            role=CustomUser.ROLES[2][0],
        )
        self.user_receptionist = CustomUser.objects.create(
            username='receptionist',
            email='receptionist@gmail.com',
            password='receptionist',
            first_name='receptionist',
            last_name='receptionist',
            phone='1234567890',
            role=CustomUser.ROLES[3][0],
        )
        self.user_parent = CustomUser.objects.create(
            username='parent',
            email='parent@gmail.com',
            password='parent',
            first_name='parent',
            last_name='parent',
            phone='1234567890',
            role=CustomUser.ROLES[4][0],
        )
        self.potential = CustomUser.objects.create(
            username='potential',
            email='potential@gmail.com',
            password='potential',
            first_name='potential',
            last_name='potential',
            phone='1234567890',
            role=CustomUser.ROLES[5][0],
        )
        self.teacher_member = Teacher.objects.create(
            user=CustomUser.objects.get(id=self.user_teacher.id),
        )
        self.receptionist_member = Receptionist.objects.create(
            user=CustomUser.objects.get(id=self.user_receptionist.id),
        )
        self.parent_member = Parent.objects.create(
            user=CustomUser.objects.get(id=self.user_parent.id),
            relation=Parent.GUARDIAN_RELATION[4][0],
        )
        self.sales_manager_member = SalesManager.objects.create(
            id=1,
            user=CustomUser.objects.get(id=self.user_sales_manager.id),
            total_sold=0,
        )
        sales_manager_pk = SalesManager.objects.get(pk=1)
        # create student
        self.student = Student.objects.create(
            first_name='student1FirstName',
            last_name='student1Surname',
            birthday='2000-01-01',
            address='student1Address',
            enrolled='01/01/2000',
            classes_left=50,
            notes='student1Notes',
        )

        self.student2 = Student.objects.create(
            first_name='student1FirstName',
            last_name='student1Surname',
            birthday='2000-01-01',
            address='student1Address',
            enrolled='01/01/2000',
            classes_left=50,
            notes='student1Notes',
        )
        self.student.parent.add(Parent.objects.get(id=1))
        self.student.sales_manager.add(sales_manager_pk)
        # create lessons
        self.lesson = Lesson.objects.create(
            date='2019-01-01',
            time=TIME_PERIODS[0][0],
            subject=SUBJECTS[0][0],
        )
        self.lesson.teachers.add(Teacher.objects.get(id=1))
        self.lesson.students.add(Student.objects.get(id=1))

    def test_get_time(self):
        """Test the get_time method of the Lesson model."""
        self.assertEqual(self.lesson.get_time(), TIME_PERIODS[0][1])

    def test_get_subject(self):
        """Test the get_subject method of the Lesson model."""
        self.assertEqual(self.lesson.get_subject(), SUBJECTS[0][1])

    def test_get_subjects(self):
        """Test the get_subjects method of the Lesson model."""
        unpacked_subjects = {x[0]: x[1] for x in SUBJECTS}
        self.assertEqual(self.lesson.get_subjects(), unpacked_subjects)

    def test_get_time_periods(self):
        """Test the get_time_periods method of the Lesson model."""
        unpacked_time_periods = {x[0]: x[1] for x in TIME_PERIODS}
        self.assertEqual(self.lesson.get_time_periods(), unpacked_time_periods)

    def test_get_teachers(self):
        """Test the get_teachers method of the Lesson model."""
        self.assertEqual(self.lesson.get_teachers()[0], self.teacher_member)

    def test_get_students(self):
        """Test the get_students method of the Lesson model."""
        self.assertEqual(self.lesson.get_students()[0], self.student)
