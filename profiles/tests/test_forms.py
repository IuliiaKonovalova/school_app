from django.test import SimpleTestCase, TestCase
from profiles.forms import (
    SimpleSignupForm,
    NewApplicationForm,
    UserProfileEditForm,
    ParentRelationForm
)
from profiles.models import CustomUser, Parent


class TestForms(TestCase):
    """Test the forms in the profiles app."""
    def test_simple_signup_form(self):
        """Test the simple signup form."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
        self.assertEqual(
            form.fields['username'].widget.attrs['placeholder'],
            'Username'
        )
        self.assertEqual(
            form.fields['first_name'].widget.attrs['placeholder'],
            'First Name'
        )
        self.assertEqual(
            form.fields['last_name'].widget.attrs['placeholder'],
            'Last Name'
        )
        self.assertEqual(
            form.fields['phone'].widget.attrs['placeholder'],
            'Phone Number'
        )
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'],
            'E-mail address'
        )
        self.assertEqual(
            form.fields['role'].initial,
            5
        )

    def test_simple_signup_form_invalid_email(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_password(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'usename@gmail.com',
                'password1': 'password',
                'password2': 'password',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_no_data(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)

    def test_simple_signup_form_invalid_no_username(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': '',
                'email': 'username@mail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_no_email(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': '',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_no_password(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username@gmail.com',
                'password1': '',
                'password2': '',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_simple_signup_form_invalid_no_first_name(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username@gmail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': '',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_no_last_name(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username@gmail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': '',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_simple_signup_form_invalid_no_phone(self):
        """Test the simple signup form with invalid data."""
        form = SimpleSignupForm(
            data={
                'username': 'username',
                'email': 'username@gmail.com',
                'password1': 'passwor34Rd',
                'password2': 'passwor34Rd',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_new_application_form(self):
        """Test the new application form."""
        form = NewApplicationForm(
            data={
                'role': CustomUser.ROLES[3][0],
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_new_application_form_invalid_no_role(self):
        """Test the new application form with invalid data."""
        form = NewApplicationForm(
            data={
                'role': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_new_application_form_invalid_wrong_role(self):
        """Test the new application form with invalid data."""
        form = NewApplicationForm(
            data={
                'role': 'wrong_role',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_new_application_form_invalid_no_data(self):
        """Test the new application form with invalid data."""
        form = NewApplicationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_user_profile_edit_form(self):
        """Test the user profile edit form."""
        form = UserProfileEditForm(
            data={
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_user_profile_edit_form_invalid_no_first_name(self):
        """Test the user profile edit form with invalid data."""
        form = UserProfileEditForm(
            data={
                'first_name': '',
                'last_name': 'last_name',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_user_profile_edit_form_invalid_no_last_name(self):
        """Test the user profile edit form with invalid data."""
        form = UserProfileEditForm(
            data={
                'first_name': 'first_name',
                'last_name': '',
                'phone': '456987786',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_user_profile_edit_form_invalid_no_phone(self):
        """Test the user profile edit form with invalid data."""
        form = UserProfileEditForm(
            data={
                'first_name': 'first_name',
                'last_name': 'last_name',
                'phone': '',
                'role': CustomUser.ROLES[5][0]
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_user_profile_edit_form_invalid_no_data(self):
        """Test the user profile edit form with invalid data."""
        form = UserProfileEditForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_parent_relation_form(self):
        """Test the parent relationship form."""
        form = ParentRelationForm(
            data={
                'relation': Parent.GUARDIAN_RELATION[1][0],
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_parent_relation_form_invalid_no_relation(self):
        """Test the parent relationship form with invalid data."""
        form = ParentRelationForm(
            data={
                'relation': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_parent_relation_form_invalid_wrong_relation(self):
        """Test the parent relationship form with invalid data."""
        form = ParentRelationForm(
            data={
                'relation': 'wrong_relation',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
