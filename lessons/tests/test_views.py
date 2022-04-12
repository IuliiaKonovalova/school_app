"""Tests for the views of the lessons app."""
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
        sales_manager_pk = SalesManager.objects.get(pk=1)
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
        self.student.sales_manager.add(sales_manager_pk)
        # create lesson
        self.lesson_first = Lesson.objects.create(
            date='2019-01-01',
            time=TIME_PERIODS[0][0],
            subject=SUBJECTS[0][0],
        )
        self.lesson_first.teachers.add(Teacher.objects.get(id=1))
        self.lesson_first.students.add(Student.objects.get(id=1))

    def test_lesson_view(self):
        """Test the lesson view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        self.assertEquals(response.context['lessons_time_1'].count(), 0)
        self.assertEquals(response.context['lessons_time_2'].count(), 0)
        self.assertEquals(response.context['lessons_time_3'].count(), 0)
        self.assertEquals(response.context['lessons_time_4'].count(), 0)
        self.assertEquals(response.context['lessons_time_5'].count(), 0)
        self.assertEquals(response.context['lessons_time_6'].count(), 0)
        self.assertEquals(response.context['lessons_time_7'].count(), 0)
        self.assertEquals(response.context['lessons_time_0'].first().id, 1)
        self.assertEquals(
            response.context['lessons_time_0'].first().subject, SUBJECTS[0][0]
        )
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        #  logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons_list.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # if user is not authenticated
        self.client.logout()
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_teacher_schedule_view(self):
        """Test the teacher schedule view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/teacher_schedule.html')
        self.assertEquals(response.context['lessons_time_0'].count(), 1)
        self.assertEquals(response.context['lessons_time_1'].count(), 0)
        self.assertEquals(response.context['lessons_time_2'].count(), 0)
        self.assertEquals(response.context['lessons_time_3'].count(), 0)
        self.assertEquals(response.context['lessons_time_4'].count(), 0)
        self.assertEquals(response.context['lessons_time_5'].count(), 0)
        self.assertEquals(response.context['lessons_time_6'].count(), 0)
        self.assertEquals(response.context['lessons_time_7'].count(), 0)
        self.assertEquals(response.context['lessons_time_0'].first().id, 1)
        self.assertEquals(
            response.context['lessons_time_0'].first().subject, SUBJECTS[0][0]
        )
        #  logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.teacher_schedule_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()
        # if user is not authenticated
        self.client.logout()
        response = self.client.get(self.lessons_list_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_lesson_add_get_view(self):
        """Test the lesson add get view."""
        # login as a boss
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        #  logout and login as a receptionist
        self.client.logout()
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_add.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.lesson_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_lesson_add_post_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(Student.objects.get(id=1).classes_left, 50)
        # create student
        self.student2 = Student.objects.create(
            first_name='Sam',
            last_name='Ray',
            birthday='2000-01-01',
            address='student1Address',
            enrolled='01/01/2000',
            classes_left=0,
            notes='student1Notes',
        )
        self.student.parent.add(Parent.objects.get(id=1))
        self.student.sales_manager.add(SalesManager.objects.get(id=1))
        response = self.client.post(self.lesson_add_url, {
            'date': '2022-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1, 2],
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/lessons/')
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(Lesson.objects.last().time, TIME_PERIODS[0][0])
        self.assertEquals(Lesson.objects.last().subject, SUBJECTS[0][0])
        self.assertEquals(Lesson.objects.last().teachers.count(), 1)
        self.assertEquals(Lesson.objects.last().teachers.first().id, 1)
        self.assertEquals(Lesson.objects.last().students.count(), 2)
        self.assertEquals(Lesson.objects.last().students.first().id, 2)
        self.assertEquals(Student.objects.get(id=1).classes_left, 49)
        self.assertEquals(Student.objects.get(id=2).classes_left, -1)
        self.assertEquals(
            self.client.session['messages1'],
            (
                [
                    'Unfortunately, ' +
                    Student.objects.get(id=2).first_name +
                    ' ' +
                    Student.objects.get(id=2).last_name +
                    ' does not have enough classes left. ' +
                    'However, proceed with caution and notify ' +
                    'Sales Department.'
                ]
            )
        )
        response = self.client.post(self.lesson_add_url, {
            'date': '2022-02-01',
            'time': '',
            'subject': '',
            'teachers': [1],
            'students': [1, 2],
        })
        self.assertTemplateUsed(response, 'lessons/lesson_add.html')
        # logout and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        response = self.client.post(self.lesson_add_url, {
            'date': '2023-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.post(self.lesson_add_url, {
            'date': '2024-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.post(self.lesson_add_url, {
            'date': '2025-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.post(self.lesson_add_url, {
            'date': '2026-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.post(self.lesson_add_url, {
            'date': '2027-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_lesson_edit_get_post_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lesson_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_edit.html')
        # logout and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lesson_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lesson_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lesson_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lesson_edit_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get

    def test_lesson_edit_post_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.student2 = Student.objects.create(
            first_name='Sam',
            last_name='Ray',
            birthday='2000-01-01',
            address='student1Address',
            enrolled='01/01/2000',
            classes_left=0,
            notes='student1Notes',
        )
        response = self.client.post(self.lesson_edit_url, {
            'date': '2028-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1, 2],
        })
        self.assertEquals(Student.objects.get(id=2).classes_left, -1)
        self.assertEquals(
            self.client.session['messages1'],
            (
                [
                    'Unfortunately, ' +
                    Student.objects.get(id=2).first_name +
                    ' ' +
                    Student.objects.get(id=2).last_name +
                    ' does not have enough classes left. ' +
                    'However, proceed with caution and notify ' +
                    'Sales Department.'
                ]
            )
        )
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/lessons/')
        response = self.client.post(self.lesson_add_url, {
            'date': '2022-02-01',
            'time': '',
            'subject': '',
            'teachers': [1],
            'students': 3,
        })
        self.assertTemplateUsed(response, 'lessons/lesson_add.html')
        # logout and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        response = self.client.post(self.lesson_edit_url, {
            'date': '2029-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.post(self.lesson_edit_url, {
            'date': '2030-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.post(self.lesson_edit_url, {
            'date': '2031-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.post(self.lesson_edit_url, {
            'date': '2032-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.post(self.lesson_edit_url, {
            'date': '2033-01-01',
            'time': TIME_PERIODS[0][0],
            'subject': SUBJECTS[0][0],
            'teachers': [1],
            'students': [1],
        })
        self.assertEquals(Lesson.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_lesson_delete_get_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(Student.objects.get(id=1).classes_left, 50)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_delete.html')
        # logout and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.client.logout()

    def test_lesson_delete_post_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        self.assertEquals(Student.objects.get(id=1).classes_left, 50)
        response = self.client.post(self.lesson_delete_url, {
            'pk': 'delete',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/lessons/')
        self.assertEquals(Lesson.objects.count(), 0)
        self.assertEquals(Student.objects.get(id=1).classes_left, 51)
        # logout and login as a boss
        self.client.logout()
        # create lesson
        self.lesson_first = Lesson.objects.create(
            date='2019-01-01',
            time=TIME_PERIODS[0][0],
            subject=SUBJECTS[0][0],
        )
        self.lesson_first.teachers.add(Teacher.objects.get(id=1))
        self.lesson_first.students.add(Student.objects.get(id=1))
        self.client.force_login(self.user_boss)
        response = self.client.post(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.assertEquals(Lesson.objects.count(), 1)
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.post(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.assertEquals(Lesson.objects.count(), 1)
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.post(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.assertEquals(Lesson.objects.count(), 1)
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.post(self.lesson_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
        self.assertEquals(Lesson.objects.count(), 1)
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.post(self.lesson_delete_url)

    def test_lesson_detail_view(self):
        # login as a receptionist
        self.client.force_login(self.user_receptionist)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')
        self.assertEquals(response.context['lesson'], self.lesson_first)
        self.assertEqual(response.context['lesson'].id, 1)
        self.assertEqual(response.context['lesson'].teachers.count(), 1)
        self.assertEqual(response.context['lesson'].students.count(), 1)
        # logout and login as a boss
        self.client.logout()
        self.client.force_login(self.user_boss)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')
        # logout and login as a teacher
        self.client.logout()
        self.client.force_login(self.user_teacher)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')
        # logout and login as a parent
        self.client.logout()
        self.client.force_login(self.user_parent)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')
        # logout and login as a sales manager
        self.client.logout()
        self.client.force_login(self.user_sales_manager)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lesson_detail.html')
        # logout and login as a potential
        self.client.logout()
        self.client.force_login(self.potential)
        response = self.client.get(self.lesson_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/access_limitation.html')
