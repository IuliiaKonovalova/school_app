"""Testing cases for the sales' models."""
from django.test import TestCase
from sales.models import Sales
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)


class SalesModelTest(TestCase):
    """Test the models for the sales app."""
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

        self.sales_deal = Sales.objects.create(
            sold_by = self.sales_manager_member,
            sold_to = self.parent_member,
            amount = 10,
            date = '2020-01-01',
            student_id = 1,
        )

    def test_sales_str(self):
        """Test the sales string representation."""
        self.assertEqual(
            (
                str(self.sales_deal.sold_by) +
                ' sold ' +
                str(self.sales_deal.amount) +
                ' classes to ' +
                str(self.sales_deal.sold_to)
            ),
            'Kate Paterson sold 10 classes to Susan Black'
        )
