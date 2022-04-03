import email
from multiprocessing import parent_process
from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import (
    CustomUser,
    Teacher,
    Receptionist,
    SalesManager,
    Parent
)
from students.models import Student
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
            # get the parent user from the CustomUser model
            user = CustomUser.objects.get(id = self.user_parent.id),
            relation = Parent.GUARDIAN_RELATION[4][0],
        )
        self.sales_manager_member = SalesManager.objects.create(
            # get the sales manager user from the CustomUser model
            id = 1,
            user = CustomUser.objects.get(id = self.user_sales_manager.id),
            total_sold = 0,
        )
        sales_manager_pk = SalesManager.objects.get(pk=1)

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
        self.student.sales_manager.add(sales_manager_pk)



    def test_user_profile_view(self):
        """Test the user_profile view."""
        # login as a boss
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
        # logout as a teacher
        self.client.logout()
        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.user_profile_url = self.user_profile_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')
        # logout as a sales manager
        self.client.logout()
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.user_profile_url = self.user_profile_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')
        # logout as a receptionist
        self.client.logout()
        # login as a parent
        self.client.force_login(self.user_parent)
        self.user_profile_url = self.user_profile_url.replace('username', self.user_parent.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')
        # check that this view sends context with the user's profile
        self.assertEquals(response.context['user'], self.user_parent)
        # logout as a parent
        self.client.logout()
        # login as a potential
        self.client.force_login(self.potential)
        self.user_profile_url = self.user_profile_url.replace('username', self.potential.username)
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile.html')
        # logout as a potential
        self.client.logout()



    def test_user_profile_edit_view(self):
        """Test the user_profile_edit view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_boss.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a boss
        self.client.logout()

        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a teacher
        self.client.logout()

        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a sales manager
        self.client.logout()

        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a receptionist
        self.client.logout()

        # login as a parent
        self.client.force_login(self.user_parent)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_parent.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a parent
        self.client.logout()

        # login as a potential
        self.client.force_login(self.potential)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.potential.username)
        response = self.client.get(self.user_profile_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/user_profile_edit.html')
        # logout as a potential
        self.client.logout()



    def test_user_profile_edit_view_post(self):
        """Test the user_profile_edit view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.user_profile_edit_url = self.user_profile_edit_url.replace('username', self.user_boss.username)
        response = self.client.post(self.user_profile_edit_url, {
            'username': self.user_boss.username,
            'email': self.user_boss.email,
            'first_name': 'newBossName',
            'last_name': 'newBossLastName',
            'phone': '1234567890',
            'role': self.user_boss.role,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/profiles/boss/')
        self.assertEquals(CustomUser.objects.get(id=self.user_boss.id).first_name, 'newBossName')
        self.assertEquals(CustomUser.objects.get(id=self.user_boss.id).last_name, 'newBossLastName')
        self.assertEquals(CustomUser.objects.get(id=self.user_boss.id).email, 'boss@gmail.com')
        self.assertEquals(CustomUser.objects.get(id=self.user_boss.id).phone, '1234567890')
        self.assertEquals(CustomUser.objects.get(id=self.user_boss.id).role, CustomUser.ROLES[0][0])
        # logout as a boss
        self.client.logout()

    def test_new_applications_view_get(self):
        """Test the new_applications view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.new_applications_url = self.new_applications_url.replace('username', self.user_boss.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/new_applications.html')
        # logout as a boss
        self.client.logout()

        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.new_applications_url = self.new_applications_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher
        self.client.logout()

        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.new_applications_url = self.new_applications_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/new_applications.html')
        # logout as a sales manager
        self.client.logout()

        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.new_applications_url = self.new_applications_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist
        self.client.logout()
        
        # login as a parent
        self.client.force_login(self.user_parent)
        self.new_applications_url = self.new_applications_url.replace('username', self.user_parent.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent
        self.client.logout()
        
        # login as a potential
        self.client.force_login(self.potential)
        self.new_applications_url = self.new_applications_url.replace('username', self.potential.username)
        response = self.client.get(self.new_applications_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a potential
        self.client.logout()

    def test_new_application_view_get(self):
        """Test the new_application view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_boss.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/application_detail.html')
        # logout as a boss
        self.client.logout()

        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher
        self.client.logout()

        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/application_detail.html')
        # logout as a sales manager
        self.client.logout()

        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist
        self.client.logout()

        # login as a parent
        self.client.force_login(self.user_parent)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_parent.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent
        self.client.logout()

        # login as a potential
        self.client.force_login(self.potential)
        self.application_detail_url = self.application_detail_url.replace('username', self.potential.username)
        response = self.client.get(self.application_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a potential
        self.client.logout()

    def test_new_application_view_post(self):
        """Test the new_application view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_boss.username)
        response1 = self.client.post(self.application_detail_url, {'role': 'teacher'})
        self.assertEquals(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'profiles/access_limitation.html')
        response2 = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, 'profiles/application_detail.html')
        # logout as a boss
        self.client.logout()

        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_teacher.username)
        response = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher
        self.client.logout()

        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_sales_manager.username)
        response = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a sales manager
        self.client.logout()

        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_receptionist.username)
        response = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist
        self.client.logout()

        # login as a parent
        self.client.force_login(self.user_parent)
        self.application_detail_url = self.application_detail_url.replace('username', self.user_parent.username)
        response = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent
        self.client.logout()
        
        # login as a potential
        self.client.force_login(self.potential)
        self.application_detail_url = self.application_detail_url.replace('username', self.potential.username)
        response = self.client.post(self.application_detail_url, {'role': 1})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a potential
        self.client.logout()

    def test_application_delete_view_get(self):
        """Test the application_delete view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.application_delete_url = self.application_delete_url.replace('username', self.user_boss.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/application_delete.html')
        # logout as a boss
        self.client.logout()

        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.application_delete_url = self.application_delete_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a teacher
        self.client.logout()

        # login as a sales manager
        self.client.force_login(self.user_sales_manager)
        self.application_delete_url = self.application_delete_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/profiles/sales_manager/applications/1/')
        # logout as a sales manager
        self.client.logout()

        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.application_delete_url = self.application_delete_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a receptionist
        self.client.logout()

        # login as a parent
        self.client.force_login(self.user_parent)
        self.application_delete_url = self.application_delete_url.replace('username', self.user_parent.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a parent
        self.client.logout()

        # login as a potential
        self.client.force_login(self.potential)
        self.application_delete_url = self.application_delete_url.replace('username', self.potential.username)
        response = self.client.get(self.application_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout as a potential
        self.client.logout()

    def test_application_delete_view_post(self):


    def test_search_members_view(self):
        """Test the search_members view."""
        # Login as boss
        self.client.force_login(self.user_boss)
        self. search_members_url = self.search_members_url.replace('username', self.user_boss.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_boss
        self.client.logout()
        # login as teacher
        self.client.force_login(self.user_teacher)
        self.search_members_url = self.search_members_url.replace('username', self.user_teacher.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_teacher
        self.client.logout()
        # login as sales_manager
        self.client.force_login(self.user_sales_manager)
        self.search_members_url = self.search_members_url.replace('username', self.user_sales_manager.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_sales_manager
        self.client.logout()
        # login as receptionist
        self.client.force_login(self.user_receptionist)
        self.search_members_url = self.search_members_url.replace('username', self.user_receptionist.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_receptionist
        self.client.logout()
        # login as parent
        self.client.force_login(self.user_parent)        
        self.search_members_url = self.search_members_url.replace('username', self.user_parent.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout user_parent
        self.client.logout()
        # login as potential
        self.client.force_login(self.potential)
        self.search_members_url = self.search_members_url.replace('username', self.potential.username)
        response = self.client.get(self.search_members_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout user_potential
        self.client.logout()

    def test_search_members_POST(self):
        """Test the search_members view."""
        # Login as boss
        self.client.force_login(self.user_boss)
        self. search_members_url = self.search_members_url.replace('username', self.user_boss.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_boss
        self.client.logout()
        # login as teacher
        self.client.force_login(self.user_teacher)
        self.search_members_url = self.search_members_url.replace('username', self.user_teacher.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_teacher
        self.client.logout()
        # login as sales_manager
        self.client.force_login(self.user_sales_manager)
        self.search_members_url = self.search_members_url.replace('username', self.user_sales_manager.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_sales_manager
        self.client.logout()
        # login as receptionist
        self.client.force_login(self.user_receptionist)
        self.search_members_url = self.search_members_url.replace('username', self.user_receptionist.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/search_members.html')
        # logout user_receptionist
        self.client.logout()
        # login as parent
        self.client.force_login(self.user_parent)
        self.search_members_url = self.search_members_url.replace('username', self.user_parent.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout user_parent
        self.client.logout()
        # login as potential
        self.client.force_login(self.potential)
        self.search_members_url = self.search_members_url.replace('username', self.potential.username)
        response = self.client.post(self.search_members_url, {'search_term': 'role'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout user_potential
        self.client.logout()







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

    def test_delete_member_POST(self):
        """Test the delete_member view."""
        self.client.force_login(self.user_boss)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 302)
        self.search_members_url = self.search_members_url.replace('username', self.user_boss.username)
        self.assertRedirects(response, self.search_members_url)
        # logout as a boss
        self.client.logout()
        # login as a teacher
        self.client.force_login(self.user_teacher)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 404)
        # logout as a teacher
        self.client.logout()
        # login as a sales_manager
        self.client.force_login(self.user_sales_manager)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 404)
        # logout as a sales_manager
        self.client.logout()
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 404)
        # logout as a receptionist
        self.client.logout()
        # login as a parent
        self.client.force_login(self.user_parent)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 404)
        # logout as a parent
        self.client.logout()
        # login as a potential
        self.client.force_login(self.potential)
        self.delete_member_url = self.delete_member_url.replace('username', self.user.username)
        response = self.client.post(self.delete_member_url, {'delete_member': 'delete'})
        self.assertEquals(response.status_code, 404)
