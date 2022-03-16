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
                teacher = form.cleaned_data['teachers'][0]
                student = form.cleaned_data['students'][0]
                student.classes_left -= 1
                student.save()
                lesson.save()
                form.save_m2m()
                lesson.teachers.add(teacher)
                lesson.students.add(student)
                lesson.save()
                return HttpResponseRedirect(
                    reverse('lessons_list')
                    )
            return render(
                request,
                'lessons/lesson_add.html',
                {'form': form}
                )
