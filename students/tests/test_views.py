"""Test for the views in the students app."""
from django.test import TestCase, Client
from django.urls import reverse
from students.models import Student
from profiles.models import (
    CustomUser,
    SalesManager,
    Parent
)


class TestStudentsViews(TestCase):
    """Test the views in the students app."""

    def setUp(self):
        """Set up the test."""
        self.client = Client()
        self.students_url = reverse('students')
        self.student_add_url = reverse('student_add')
        self.student_detail_url = reverse('student_detail', args=[1])
        self.student_edit_url = reverse('student_edit', args=[1])
        self.student_delete_url = reverse('student_delete', args=[1])
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
        self.user_receptionist = CustomUser.objects.create(
            username='receptionist',
            email='receptionist@gmail.com',
            password='receptionist',
            first_name='receptionist',
            last_name='receptionist',
            phone='1234567890',
            role=CustomUser.ROLES[3][0],
        )
        self.user_sales_manager = CustomUser.objects.create(
            username='sales_manager',
            email='salesmanager@gmail.com',
            password='salesmanager',
            first_name='Kate',
            last_name='Paterson',
            phone='1234567890',
            role=CustomUser.ROLES[2][0],
        )
        self.user_parent = CustomUser.objects.create(
            username='parent',
            email='parent@gmail.com',
            password='parent',
            first_name='Susan',
            last_name='Black',
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
        self.parent_member = Parent.objects.create(
            user=CustomUser.objects.get(id=self.user_parent.id),
            relation=Parent.GUARDIAN_RELATION[4][0],
        )
        self.sales_manager_member = SalesManager.objects.create(
            id=1,
            user=CustomUser.objects.get(id=self.user_sales_manager.id),
            total_sold=0,
        )
        # create student
        self.student = Student.objects.create(
            first_name='student1FirstName',
            last_name='student1Surname',
            birthday='2000-01-01',
            address='student1Address',
            enrolled='01/01/2000',
            classes_left=50,
            notes='student1Notes',
        )
        self.student.parent.add(Parent.objects.get(id=1))
        self.student.sales_manager.add(SalesManager.objects.get(id=1))

    def test_students_add_get_view(self):
        """Test the students_add_get_view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_boss.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_add.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_sales_manager.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_add.html')
        # logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_receptionist.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_teacher.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_parent.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.potential.username
        )
        response=self.client.get(self.student_add_url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_students_add_post_view(self):
        """Test the students_add_post_view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_boss.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student2FirstName',
            'last_name': 'student2Surname',
            'birthday': '2000-01-01',
            'address': 'student2Address',
            'classes_left': 50,
            'notes': 'student2Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 2)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/students/students/')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_sales_manager.username
        )
        self.assertEqual(Student.objects.count(), 2)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student3FirstName',
            'last_name': 'student3Surname',
            'birthday': '2010-01-01',
            'address': 'student3Address',
            'classes_left': 50,
            'notes': 'student3Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 3)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/students/students/')
        # logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_receptionist.username
        )
        self.assertEqual(Student.objects.count(), 3)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student4FirstName',
            'last_name': 'student4Surname',
            'birthday': '2000-01-01',
            'address': 'student4Address',
            'classes_left': 50,
            'notes': 'student4Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 3)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_teacher.username
        )
        self.assertEqual(Student.objects.count(), 3)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student5FirstName',
            'last_name': 'student5Surname',
            'birthday': '2000-01-01',
            'address': 'student5Address',
            'classes_left': 50,
            'notes': 'student5Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 3)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.user_parent.username
        )
        self.assertEqual(Student.objects.count(), 3)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student6FirstName',
            'last_name': 'student6Surname',
            'birthday': '2000-01-01',
            'address': 'student6Address',
            'classes_left': 50,
            'notes': 'student6Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 3)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.student_add_url = self.student_add_url.replace(
            'username',
            self.potential.username
        )
        self.assertEqual(Student.objects.count(), 3)
        response=self.client.post(self.student_add_url, {
            'first_name': 'student7FirstName',
            'last_name': 'student7Surname',
            'birthday': '2000-01-01',
            'address': 'student7Address',
            'classes_left': 50,
            'notes': 'student7Notes',
            'parent': [1],
            'sales_manager': [1],
        })
        self.assertEquals(Student.objects.count(), 3)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_students_view_get(self):
        """Test the students_view_get."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.students_url = self.students_url.replace(
            'username',
            self.user_boss.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/students.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.students_url = self.students_url.replace(
            'username',
            self.user_sales_manager.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/students.html')
        # logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.students_url = self.students_url.replace(
            'username',
            self.user_receptionist.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/students.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.students_url = self.students_url.replace(
            'username',
            self.user_teacher.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/students.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.students_url = self.students_url.replace(
            'username',
            self.user_parent.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.students_url = self.students_url.replace(
            'username',
            self.potential.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.students_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_student_detail_view_get(self):
        """Test the student_detail_view_get."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.user_boss.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.user_sales_manager.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        # logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.user_receptionist.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.user_teacher.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.user_parent.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_detail.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.student_detail_url = self.student_detail_url.replace(
            'username',
            self.potential.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_student_edit_view_get(self):
        """Test the student_edit_view_get."""
        # login as a boss
        self.client.force_login(self.user_boss)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.user_boss.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_edit.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.user_sales_manager.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_edit.html')
        # logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.user_receptionist.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.user_teacher.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.user_parent.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        self.student_edit_url = self.student_edit_url.replace(
            'username',
            self.potential.username
        )
        self.assertEqual(Student.objects.count(), 1)
        response=self.client.get(self.student_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    # def test_student_edit_view_post(self):
