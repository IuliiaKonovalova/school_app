"""Tests for the forms in the sales app."""
from django.test import TestCase
from sales.forms import SalesForm
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)
from students.models import Student


class SalesFormTest(TestCase):
    """Test the forms in the sales app."""
    def setUp(self):
        """Set up the test."""
        # create sales
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
        form = SalesForm()
        expected = ['sold_to', 'amount', 'student']
        actual = list(form.fields.keys())
        self.assertEqual(expected, actual)
        self.assertEqual(len(form.fields), 3)

    def test_form_has_labels(self):
        """Test the form has labels."""
        form = SalesForm()
        self.assertTrue(form.fields['sold_to'].label == 'Sold to')
        self.assertTrue(form.fields['amount'].label == 'Amount')
        self.assertTrue(form.fields['student'].label == None)

    def test_form_is_valid(self):
        """Test the form has data."""
        form = SalesForm({
            'sold_to': self.parent_member.id,
            'amount': 10,
            'student': 1,
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_form_has_no_data(self):
        """Test the form has no data."""
        form = SalesForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_form_has_no_data_amount(self):
        """Test the form has no data for amount."""
        form = SalesForm({
            'sold_to': self.parent_member.id,
            'amount': '',
            'student': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_form_has_no_data_sold_to(self):
        """Test the form has no data for sold_to."""
        form = SalesForm({
            'sold_to': '',
            'amount': 10,
            'student': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
    def test_form_has_no_data_student(self):

        """Test the form has no data for student."""
        form = SalesForm({
            'sold_to': self.parent_member.id,
            'amount': 10,
            'student': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
