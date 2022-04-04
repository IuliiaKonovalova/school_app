"""Tests for the forms in the students app."""
from django.test import TestCase
from students.forms import AddStudentForm
from students.models import Student
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)


class TestAddStudentForm(TestCase):
    """Test the AddStudentForm."""
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

    def test_form_has_fields(self):
        """Test the form has fields."""
        form = AddStudentForm()
        expected = [
            'first_name',
            'last_name',
            'parent',
            'birthday',
            'address',
            'classes_left',
            'sales_manager',
            'notes'
        ]
        self.assertSequenceEqual(expected, list(form.fields))
        actual = list(form.fields.keys())
        self.assertEqual(expected, actual)
        self.assertEqual(len(form.fields), 8)

    def test_form_validation_for_blank_input(self):
        """Test form validation for blank input."""
        form = AddStudentForm(data={
            'first_name': '',
            'last_name': '',
            'parent': '',
            'birthday': '',
            'address': '',
            'classes_left': '',
            'sales_manager': '',
            'notes': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['first_name'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['last_name'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['parent'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['birthday'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['sales_manager'],
            ["This field is required."]
        )

    def test_form_is_valid(self):
        """Test form is valid."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_form_no_data(self):
        """Test form no data."""
        form = AddStudentForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_form_no_first_name(self):
        """Test form no first name."""
        form = AddStudentForm(data={
            'first_name': '',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['first_name'],
            ["This field is required."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_no_last_name(self):
        """Test form no last name."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': '',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['last_name'],
            ["This field is required."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_no_parent(self):
        """Test form no parent."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': '',
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['parent'],
            ["This field is required."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_no_birthday(self):
        """Test form no birthday."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['birthday'],
            ["This field is required."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_no_sales_manager(self):
        """Test form no sales manager."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': '',
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['sales_manager'],
            ["This field is required."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_invalid_birthday(self):
        """Test form invalid birthday."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-32',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['birthday'],
            ["Enter a valid date."]
        )
        self.assertEquals(len(form.errors), 1)

    def test_form_no_classes_left(self):
        """Test form invalid classes left."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': '',
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_form_no_address(self):
        """Test form no address."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': '',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': 'student1Notes'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_form_no_notes(self):
        """Test form no notes."""
        form = AddStudentForm(data={
            'first_name': 'student1FirstName',
            'last_name': 'student1Surname',
            'parent': [self.parent_member.id],
            'birthday': '2000-01-01',
            'address': 'student1Address',
            'classes_left': 50,
            'sales_manager': [self.user_sales_manager.id],
            'notes': ''
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
