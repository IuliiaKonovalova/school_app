"""Testing cases for the students' models."""
from django.test import TestCase
from students.models import Student
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)


class StudentModelTest(TestCase):
    """Test the models for the students app."""
    def setUp(self):
        """Set up the test."""
        # create users
        self.user_sales_manager = CustomUser.objects.create(
            username='sales_manager',
            email = 'salesmanager@gmail.com',
            password = 'salesmanager',
            first_name = 'Kate',
            last_name = 'Paterson',
            phone = '1234567890',
            role = CustomUser.ROLES[2][0],
        )
        self.user_parent = CustomUser.objects.create(
            username='parent',
            email = 'parent@gmail.com',
            password = 'parent',
            first_name = 'Susan',
            last_name = 'Black',
            phone = '1234567890',
            role = CustomUser.ROLES[4][0],
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
        self.student.parent.add(Parent.objects.get(id=1))
        self.student.sales_manager.add(SalesManager.objects.get(id=1))

    def test_has_classes_left(self):
        """Test the has_classes_left method."""
        self.assertEquals(self.student.has_classes_left(), False)
