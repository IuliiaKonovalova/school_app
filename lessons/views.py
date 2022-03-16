"""Views for the lessons app."""
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
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
            return render(
                request,
                'lessons/lessons_list.html',
                {'lessons': lessons}
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