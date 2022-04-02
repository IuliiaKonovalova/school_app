import email
from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import (
    CustomUser,
    Teacher,
    Receptionist,
    SalesManager,
    Parent
)
import json


class TestViews(TestCase):
    """Test the views for the profiles app."""
    def setUp(self):
        """Set up the test."""
        self.client = Client()
        self.user_profile_url = reverse('user_profile', args=['username'])
        self.search_members_url = reverse('search_members', args=['username'])
        self.user_profile_edit_url = reverse('user_profile_edit', args=['username'])
        self.user_profile_edit_password_url = reverse('user_profile_change_password', args=['username'])
        self.new_applications_url = reverse('new_applications', args=['username'])
        self.application_detail_url = reverse('application_detail', args=['username', '1'])
        self.application_delete_url = reverse('application_delete', args=['username', '1'])
        self.delete_member_url = reverse('delete_member', args=['username'])
        self.add_relation_url = reverse('add_relation')
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@potential.com',
            password='Testuser123',
            first_name='test',
            last_name='user',
            phone='1234567890',
            role = CustomUser.ROLES[5][0],
        )

        # self.client.force_login(self.user)


        self.user_boss = CustomUser.objects.create(
            username='boss',
            email='boss@gmail.com',
            password='boss',
            first_name='boss',
            last_name='boss',
            phone='1234567890',
            role = CustomUser.ROLES[0][0],
        )

        self.client.force_login(self.user_boss)
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
            first_name = 'parent',
            last_name = 'parent',
            phone = '1234567890',
            role = CustomUser.ROLES[4][0],
        )



    def test_user_profile_view(self):
        """Test the user_profile view."""
        self.client.force_login(self.user_boss)
        self.user_profile_url = self.user_profile_url.replace('username', self.user_boss.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')
        # logout as a boss
        self.client.logout()
        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.user_profile_url = self.user_profile_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')


    def test_user_profile_edit_view(self):
        """Test the user_profile_edit view."""
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')

    def test_search_members_view(self):
        """Test the search_members view."""
        response = self.client.get(self.search_members_url)
        # Login as boss
        self.client.force_login(self.user_boss)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_boss
        self.client.logout()
        # login as teacher
        self.client.force_login(self.user_teacher)
        # response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_teacher
        self.client.logout()
        # login as sales_manager
        self.client.force_login(self.user_sales_manager)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_sales_manager
        self.client.logout()
        # login as receptionist
        self.client.force_login(self.user_receptionist)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_receptionist
        self.client.logout()
        # login as parent
        self.client.force_login(self.user_parent)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_parent
        self.client.logout()

    def test_search_members_POST(self):
        """Test the search_members view."""
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')

    def test_delete_member_view(self):
        """Test the delete_member view."""
        self.client.force_login(self.user_boss)
        self.delete_member_url = self.delete_member_url.replace('username', self.user_boss.username)
        response = self.client.get(self.delete_member_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/delete_member.html')
        # logout as a boss
        self.client.logout()
        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.delete_member_url = self.delete_member_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.delete_member_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher
        self.client.logout()
        # login as a sales_manager
        self.client.force_login(self.user_sales_manager)
        self.delete_member_url = self.delete_member_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.delete_member_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a sales_manager
        self.client.logout()
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.delete_member_url = self.delete_member_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.delete_member_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist
        self.client.logout()
        # login as a parent
        self.client.force_login(self.user_parent)
        self.delete_member_url = self.delete_member_url.replace('username', self.user_parent.username)
        response = self.client.get(self.delete_member_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent
        self.client.logout()

