"""Tests for the forms of the lessons app."""
from django.test import TestCase, Client
from django.urls import reverse
from lessons.models import Lesson
from profiles.models import (
    CustomUser,
    Teacher,
    SalesManager,
    Receptionist,
    Parent
)
from students.models import Student
from lessons.models import TIME_PERIODS, SUBJECTS


class TestLessonForm(TestCase):
    """Test the LessonForm."""

    def setUp(self):
        """Set up the test."""
        # create users
        self.client = Client()
        self.lessons_list_url = reverse('lessons_list')
        self.lesson_add_url = reverse('lesson_add')
        self.lesson_edit_url = reverse('lesson_edit', args=['1'])
        self.lesson_delete_url = reverse('lesson_delete', args=['1'])
        self.lesson_detail_url = reverse('lesson_detail', args=['1'])
        self.teacher_schedule_url = reverse('teacher_schedule')
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
        self.teacher_member = Teacher.objects.create(
            user = CustomUser.objects.get(id=self.user_teacher.id),
        )
        self.receptionist_member = Receptionist.objects.create(
            user = CustomUser.objects.get(id=self.user_receptionist.id),
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
        sales_manager_pk = SalesManager.objects.get(pk=1)
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
        self.student.sales_manager.add(sales_manager_pk)

        self.lesson_first = Lesson.objects.create(
            date = '2019-01-01',
            time= TIME_PERIODS[0][0],
            subject = SUBJECTS[0][0],
        )
        self.lesson_first.teachers.add(Teacher.objects.get(id=1))
        self.lesson_first.students.add(Student.objects.get(id=1))
    
    def test_lesson_view(self):
        """Test the lesson view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEqual(response.context['lessons_time_0'].count(), 1)
        self.assertEqual(response.context['lessons_time_1'].count(), 0)
        self.assertEqual(response.context['lessons_time_2'].count(), 0)
        self.assertEqual(response.context['lessons_time_3'].count(), 0)
        self.assertEqual(response.context['lessons_time_4'].count(), 0)
        self.assertEqual(response.context['lessons_time_5'].count(), 0)
        self.assertEqual(response.context['lessons_time_6'].count(), 0)
        self.assertEqual(response.context['lessons_time_7'].count(), 0)
        self.assertEqual(response.context['lessons_time_0'].first().id, 1)
        self.assertEqual(response.context['lessons_time_0'].first().subject, SUBJECTS[0][0])
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEqual(response.context['lessons_time_0'].count(), 1)
        #  logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEqual(response.context['lessons_time_0'].count(), 1)
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEqual(response.context['lessons_time_0'].count(), 1)
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEqual(response.context['lessons_time_0'].count(), 1)
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.lessons_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')



        # self.assertEqual(response.context['lessons'][0].id, 1)
        # self.assertEqual(response.context['lessons'][0].date, '2019-01-01')
        # self.assertEqual(response.context['lessons'][0].time, '08:00:00')
        # self.assertEqual(response.context['lessons'][0].subject, 'Math')
        # self.assertEqual(response.context['lessons'][0].teachers.count(), 1)
        # self.assertEqual(response.context['lessons'][0].teachers[0].id, 1)
        # self.assertEqual(response.context['lessons'][0].teachers[0].user.username, 'teacher')
        # self.assertEqual(response.context['lessons'][0].students.count(), 1)
        # self.assertEqual(response.context['lessons'][0].students[0].id, 1)
        # self.assertEqual(response.context['lessons'][0].students[0].first_name, 'student1FirstName')
        # self.assertEqual(response.context['lessons'][0].students[0].last_name, 'student1Surname')
        # self.assertEqual(response.context['lessons'][0].students[0].parent.count(), 1)
        # self.assertEqual(response.context['lessons'][0].students[0].parent[0].id, 1)
