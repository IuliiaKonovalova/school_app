"""Views for the lessons app."""
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from .models import Lesson
from .forms import LessonForm
from profiles.models import Teacher


class LessonsView(View):
    """Lessons View"""
    def get(self, request, *args, **kwargs):
        """Receive lessons list"""
        if request.user.is_authenticated:
            if request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )
            else:
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
                if 'messages1' in request.session:
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


class TeacherScheduleView(View):
    """Teacher Schedule View"""
    def get(self, request, *args, **kwargs):
        """Receive lessons list for a teacher in session"""
        if request.user.is_authenticated:
            if request.user.role == 1:
                teacher = get_object_or_404(Teacher, user=request.user)
                lessons = Lesson.objects.filter(
                    teachers__in=[teacher]).distinct()
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
                }
                return render(
                    request,
                    'lessons/teacher_schedule.html',
                    context
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )
        return HttpResponseRedirect(reverse('home'))


class LessonAddView(View):
    """Lesson Add View"""
    def get(self, request):
        """Receive lesson add form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
                form = LessonForm()
                return render(
                    request,
                    'lessons/lesson_add.html',
                    {'form': form}
                    )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )

    def post(self, request):
        """Receive lesson add form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
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
                                ' does not have enough classes left. ' +
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
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )


class LessonEditView(View):
    """Lesson Edit View"""
    def get(self, request, pk):
        """Receive lesson edit form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
                lesson = get_object_or_404(Lesson, pk=pk)
                form = LessonForm(instance=lesson)
                return render(
                    request,
                    'lessons/lesson_edit.html',
                    {'form': form, 'lesson': lesson}
                    )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )

    def post(self, request, pk):
        """Receive lesson edit form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
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
                                ' does not have enough classes left. ' +
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
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )


class LessonDeleteView(View):
    """Lesson Delete View"""
    def get(self, request, pk):
        """Receive lesson delete form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
                lesson = get_object_or_404(Lesson, pk=pk)
                return render(
                    request,
                    'lessons/lesson_delete.html',
                    {'lesson': lesson}
                    )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )

    def post(self, request, pk):
        """Receive lesson delete form"""
        if request.user.is_authenticated:
            if request.user.role == 3:
                lesson = get_object_or_404(Lesson, pk=pk)
                students = lesson.students.all()
                for student in students:
                    student.classes_left += 1
                    student.save()
                lesson.delete()
                return HttpResponseRedirect(
                    reverse('lessons_list')
                    )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )


class LessonDetailView(View):
    """Lesson Detail View"""
    def get(self, request, pk):
        """Receive lesson detail"""
        if request.user.is_authenticated:
            if request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html',
                )
            else:
                lesson = get_object_or_404(Lesson, pk=pk)
                return render(
                    request,
                    'lessons/lesson_detail.html',
                    {'lesson': lesson}
                    )
