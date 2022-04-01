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
        self.assertEquals(self.user.role, CustomUser.ROLES[5][0])

    def test_get_role_choices(self):
        """Test the get role choices."""
        self.assertEquals('potential user', CustomUser.ROLES[5][1])

    def test_teacher_model(self):
        """Test the teacher model."""
        self.user.role = CustomUser.ROLES[1][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[1][0])
    
    def test_receptionist_model(self):
        """Test the receptionist model."""
        self.user.role = CustomUser.ROLES[2][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[2][0])

    def test_sales_manager_model(self):
        """Test the sales manager model."""
        self.user.role = CustomUser.ROLES[3][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[3][0])
        self.assertEquals(self.user.groups.filter(name='sales_manager').total_sold.count(), 0)
