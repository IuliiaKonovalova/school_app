"""Views for the lessons app."""
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from profiles.models import Teacher
from students.models import Student
from .forms import LessonForm


class LessonAddView(View):
    """Lesson Add View"""
    def get(self, request):
        """Receive lesson add form"""
        if request.user.is_authenticated and request.user.role == 3:
            form = LessonForm()

            # form.fields['teachers'].queryset = Teacher.objects.exclude(lessons__date=form.fields['date'].initial).exclude(lessons__time_period=form.fields['time_period'].initial)
            # form.fields['students'].queryset = Student.objects.exclude(lessons__date=form.fields['date'].initial).exclude(lessons__time_period=form.fields['time_period'].initial)
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
                teacher = form.cleaned_data['teacher'][0]
                student = form.cleaned_data['student'][0]
                lesson.save()
                form.save_m2m()
                lesson.teacher.add(teacher)
                lesson.student.add(student)
                lesson.save()
                return HttpResponseRedirect(
                    reverse('lessons')
                    )
            return render(
                request,
                'lessons/lesson_add.html',
                {'form': form}
                )
