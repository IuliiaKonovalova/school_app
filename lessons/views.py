"""Views for the lessons app."""
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from datetime import datetime
from profiles.models import Teacher
from students.models import Student
from .models import Lesson
from .forms import LessonForm



class LessonsView(View):
    """Lessons View"""
    def get(self, request, *args, **kwargs):
        """Receive lessons list"""
        if request.user.is_authenticated and request.user.role != 5:
            lessons = Lesson.objects.all()
            today_lessons = lessons.filter(date=datetime.now().date())
            dates = lessons.values_list('date', flat=True).distinct()
            # get lessons by time:
            lessons_time_0 = lessons.filter(time=0)
            lessons_time_1 = lessons.filter(time=1)
            lessons_time_2 = lessons.filter(time=2)
            lessons_time_3 = lessons.filter(time=3)
            lessons_time_4 = lessons.filter(time=4)
            lessons_time_5 = lessons.filter(time=5)
            lessons_time_6 = lessons.filter(time=6)
            lessons_time_7 = lessons.filter(time=7)
            context = {
                'lessons_time_0': lessons_time_0,
                'lessons_time_1': lessons_time_1,
                'lessons_time_2': lessons_time_2,
                'lessons_time_3': lessons_time_3,
                'lessons_time_4': lessons_time_4,
                'lessons_time_5': lessons_time_5,
                'lessons_time_6': lessons_time_6,
                'lessons_time_7': lessons_time_7,
                'lessons': lessons,
                'today_lessons': today_lessons,
                'dates': dates
            }

            return render(
                request,
                'lessons/lessons_list.html',
                context
                )
        return HttpResponseRedirect(reverse('home'))


class LessonAddView(View):
    """Lesson Add View"""
    def get(self, request):
        """Receive lesson add form"""
        if request.user.is_authenticated and request.user.role == 3:
            form = LessonForm()
            return render(
                request,
                'lessons/lesson_add.html',
                {'form': form}
                )


    def post(self, request):
        """Receive lesson add form"""
        if request.user.is_authenticated and request.user.role == 3:
            form = LessonForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                lesson = form.save(commit=False)
                students = form.cleaned_data['students']
                for student in students:
                    student.classes_left -= 1
                    student.save()
                lesson.save()
                form.save_m2m()
                lesson.save()
                return HttpResponseRedirect(
                    reverse('lessons_list')
                    )
            return render(
                request,
                'lessons/lesson_add.html',
                {'form': form}
                )


class LessonEditView(View):
    """Lesson Edit View"""
    def get(self, request, pk):
        """Receive lesson edit form"""
        if request.user.is_authenticated and request.user.role == 3:
            lesson = get_object_or_404(Lesson, pk=pk)
            form = LessonForm(instance=lesson)
            return render(
                request,
                'lessons/lesson_edit.html',
                {'form': form, 'lesson': lesson}
                )

    def post(self, request, pk):
        """Receive lesson edit form"""
        if request.user.is_authenticated and request.user.role == 3:
            lesson = get_object_or_404(Lesson, pk=pk)
            students = lesson.students.all()
            for student in students:
                student.classes_left += 1
                student.save()
            form = LessonForm(request.POST, instance=lesson)
            if form.is_valid():
                print(form.cleaned_data)
                lesson = form.save(commit=False)
                students = form.cleaned_data['students']
                for student in students:
                    student.classes_left -= 1
                    student.save()
                lesson.save()
                form.save_m2m()
                lesson.save()
                return HttpResponseRedirect(
                    reverse('lessons_list')
                    )
            return render(
                request,
                'lessons/lesson_edit.html',
                {'form': form, 'lesson': lesson}
                )


class LessonDeleteView(View):
    """Lesson Delete View"""
    def get(self, request, pk):
        """Receive lesson delete form"""
        if request.user.is_authenticated and request.user.role == 3:
            lesson = get_object_or_404(Lesson, pk=pk)
            return render(
                request,
                'lessons/lesson_delete.html',
                {'lesson': lesson}
                )

    def post(self, request, pk):
        """Receive lesson delete form"""
        if request.user.is_authenticated and request.user.role == 3:
            lesson = get_object_or_404(Lesson, pk=pk)
            students = lesson.students.all()
            for student in students:
                student.classes_left += 1
                student.save()
            lesson.delete()
            return HttpResponseRedirect(
                reverse('lessons_list')
                )


class LessonDetailView(View):
    """Lesson Detail View"""
    def get(self, request, pk):
        """Receive lesson detail"""
        if request.user.is_authenticated and request.user.role != 5:
            lesson = get_object_or_404(Lesson, pk=pk)
            return render(
                request,
                'lessons/lesson_detail.html',
                {'lesson': lesson}
                )