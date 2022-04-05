"""Testing cases for the profiles' models."""
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
        self.assertEquals(self.teacher_member.user, self.user_teacher)
        self.assertEquals(Teacher.objects.count(), 1)

    def test_receptionist_model(self):
        """Test the receptionist model."""
        self.user.role = CustomUser.ROLES[2][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[2][0])
        self.assertEquals(
            self.receptionist_member.user,
            self.user_receptionist
        )
        self.assertEquals(Receptionist.objects.count(), 1)

    def test_sales_manager_model(self):
        """Test the sales manager model."""
        self.user.role = CustomUser.ROLES[3][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[3][0])
        self.assertEquals(self.sales_manager_member.total_sold, 0)
        self.assertEquals(
            self.sales_manager_member.user,
            self.user_sales_manager
        )
        self.assertEquals(SalesManager.objects.count(), 1)

    def test_parent_model(self):
        """Test the parent model."""
        self.user.role = CustomUser.ROLES[4][0]
        self.user.save()
        self.assertEquals(self.user.role, CustomUser.ROLES[4][0])
        self.assertEquals(self.parent_member.user, self.user_parent)
        self.assertEquals(
            self.parent_member.relation,
            Parent.GUARDIAN_RELATION[4][0]
        )
        self.assertEquals(Parent.objects.count(), 1)
