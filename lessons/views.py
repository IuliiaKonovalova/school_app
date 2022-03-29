"""Views for the lessons app."""
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from .models import Lesson
from .forms import LessonForm



class LessonsView(View):
    """Lessons View"""
    def get(self, request, *args, **kwargs):
        """Receive lessons list"""
        if request.user.is_authenticated and request.user.role != 5:
            lessons = Lesson.objects.all()
            # get lessons by time:
            lessons_time_0 = lessons.filter(time=0)
            lessons_time_1 = lessons.filter(time=1)
            lessons_time_2 = lessons.filter(time=2)
            lessons_time_3 = lessons.filter(time=3)
            lessons_time_4 = lessons.filter(time=4)
            lessons_time_5 = lessons.filter(time=5)
            lessons_time_6 = lessons.filter(time=6)
            lessons_time_7 = lessons.filter(time=7)
            messages1 = []
            if request.session.has_key('messages1'):
                messages1 = request.session['messages1']
                del request.session['messages1']
            context = {
                'lessons_time_0': lessons_time_0,
                'lessons_time_1': lessons_time_1,
                'lessons_time_2': lessons_time_2,
                'lessons_time_3': lessons_time_3,
                'lessons_time_4': lessons_time_4,
                'lessons_time_5': lessons_time_5,
                'lessons_time_6': lessons_time_6,
                'lessons_time_7': lessons_time_7,
                'messages1': messages1,
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
                lesson = form.save(commit=False)
                students = form.cleaned_data['students']
                messages1 = []
                for student in students:
                    student.classes_left -= 1
                    if student.classes_left < 0:
                        messages1.append(
                            'Unfortunately, ' +
                            student.first_name +
                            ' ' +
                            student.last_name +
                            ' Does not have enough classes left. ' +
                            'However, proceed with caution and notify ' +
                            'Sales Department.'
                        )
                    student.save()
                lesson.save()
                form.save_m2m()
                lesson.save()
                request.session['messages1'] = messages1
                return HttpResponseRedirect(
                    reverse('lessons_list'),
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
                lesson = form.save(commit=False)
                students = form.cleaned_data['students']
                messages1 = []
                for student in students:
                    student.classes_left -= 1
                    if student.classes_left < 0:
                        messages1.append(
                            'Unfortunately, ' +
                            student.first_name +
                            ' ' +
                            student.last_name +
                            ' Does not have enough classes left. ' +
                            'However, proceed with caution and notify ' +
                            'Sales Department.'
                        )
                    student.save()
                lesson.save()
                form.save_m2m()
                lesson.save()
                request.session['messages1'] = messages1
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
