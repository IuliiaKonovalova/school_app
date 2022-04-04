"""Tests for the views of the sales app."""
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from sales.models import Sales
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)
from students.models import Student


class SalesViewTest(TestCase):
    """Test the sales view."""

    def setUp(self):
        """Set up the test."""
        self.client = Client()
        self.sales_list_url = reverse('sales_list')
        self.sales_form_url = reverse('sales_form')
        self.edit_sales_url = reverse('edit_sales', args=[1])
        self.delete_sales_url = reverse('delete_sales', args=[1])
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
            first_name = 'Susan',
            last_name = 'Black',
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
        self.sales_deal = Sales.objects.create(
            sold_by = self.sales_manager_member,
            sold_to = self.parent_member,
            amount = 10,
            date = '2020-01-01',
            student_id = 1,
        )

    def test_sales_get_view(self):
        """Test the sales view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sales_list.html')
        
        # logout as a boss and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sales_list.html')
        self.assertEqual(len(response.context['sales']), 1)
        # logout as a sales manager and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_sales_post_view(self):
        """Test the sales view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sales_list.html')
        self.fromdate = '2019-01-01'
        self.todate = '2022-01-02'
        self.data = {
            'fromdate': self.fromdate,
            'todate': self.todate,
        }
        response = self.client.post(self.sales_list_url, self.data)
        self.search_date = Sales.objects.filter(
            date__range=[self.fromdate, self.todate]
        )
        self.assertEquals(len(response.context['sales']), self.search_date.count())
        # logout as a boss and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sales_list.html')
        # logout as a sales manager and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.post(self.sales_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_sales_form_get_view(self):
        """Test the sales form view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.sales_form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a boss and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.sales_form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sales_form.html')
        # logout as a sales manager and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.sales_form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.sales_form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.sales_form_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.sales_form_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_edit_sales_get_view(self):
        """Test the edit sales view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.edit_sales_url = self.edit_sales_url.replace(
            'username',
            self.user_boss.username
        )
        response = self.client.get(self.edit_sales_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a boss and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.edit_sales_url = self.edit_sales_url.replace(
            'username',
            self.user_sales_manager.username
        )
        response = self.client.post(self.edit_sales_url, {
            'sold_by': 1,
            'sold_to': 1,
            'amount': 15,
            'student_id': 1,
            'date': '2019-01-01',
        })
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response, '/sales/sales_list/')

    def test_delete_sale_post(self):
        """Test the delete_sale"""
        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.assertEquals(Student.objects.get(id=1).classes_left, 50)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.user_sales_manager.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/sales/sales/')
        self.assertEquals(Sales.objects.count(), 0)
        # check classes left reduced
        self.assertEquals(Student.objects.get(id=1).classes_left, 40)
        # logout as a sales manager and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.user_boss.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a boss and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.user_teacher.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.user_receptionist.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.user_parent.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.delete_sales_url = self.delete_sales_url.replace(
            'username',
            self.potential.username
        )
        response = self.client.post(self.delete_sales_url, {'sale_id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()
