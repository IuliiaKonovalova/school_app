from django.test import TestCase
from profiles.models import (
    CustomUser,
    Teacher,
    Receptionist,
    SalesManager,
    Parent
)


class TestModels(TestCase):
    """Test the models for the profiles app."""
    def setUp(self):
        """Set up the test."""
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@potential.com',
            password='Testuser123',
            first_name='test',
            last_name='user',
            phone='1234567890',
        )

    def test_custom_user_assign_role_5(self):
        """Test the custom user assign role 5."""
        self.assertEqual(self.user.role, CustomUser.ROLES[5][0])