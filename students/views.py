"""Views for the students app."""
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View
from lessons.models import Lesson
from .models import Student
from .forms import AddStudentForm


class StudentAddView(View):
    """Student Add View"""
    def get(self, request):
        """Receive student add form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                form = AddStudentForm()
                return render(
                    request,
                    'students/student_add.html',
                    {'form': form}
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )

    def post(self, request):
        """Receive student add form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                form = AddStudentForm(request.POST)
                if form.is_valid():
                    print(form.cleaned_data)
                    student = form.save(commit=False)
                    sales_manager = form.cleaned_data['sales_manager'][0]
                    parent = form.cleaned_data['parent'][0]
                    student.save()
                    form.save_m2m()
                    student.sales_manager.add(sales_manager)
                    student.parent.add(parent)
                    student.save()
                    return HttpResponseRedirect(
                        reverse('students')
                    )
                return render(
                    request,
                    'students/student_add.html',
                    {'form': form}
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )


class StudentsView(View):
    """Students View"""
    def get(self, request, *args, **kwargs):
        """Receive students list"""
        if request.user.is_authenticated:
            if request.user.role == 4 or request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )
            else:
                students = Student.objects.all()
                context = {
                  'students': students,
                }
                return render(
                    request,
                    'students/students.html',
                    context
                )

    def post(self, request, *args, **kwargs):
        """Receive students list"""
        if request.user.is_authenticated:
            if request.user.role == 4 or request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )
            else:
                classes = request.POST.get('classes')
                if classes == 'all':
                    students = Student.objects.all()
                else:
                    students_urgent = []
                    students = Student.objects.all()
                    for student in students:
                        if student.has_classes_left():
                            students_urgent.append(student)
                    students = students_urgent
                return render(
                    request,
                    'students/students.html',
                    {'students': students}
                )


class StudentView(View):
    """Student View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student detail"""
        if request.user.is_authenticated:
            if request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )
            else:
                student = get_object_or_404(Student, pk=pk)
                lessons = Lesson.objects.filter(students__in=[student])
                return render(
                    request,
                    'students/student_detail.html',
                    {'student': student, 'lessons': lessons}
                )

    def post(self, request, pk, *args, **kwargs):
        """Receive student edit form"""
        if request.user.is_authenticated:
            if request.user.role == 5:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )
            else:
                student = get_object_or_404(Student, pk=pk)
                fromdate = request.POST.get('from_date')
                todate = request.POST.get('to_date')
                student = get_object_or_404(Student, pk=pk)
                lessons = Lesson.objects.filter(students__in=[student])
                search_items = lessons.filter(date__range=[fromdate, todate])
                return render(
                    request,
                    'students/student_detail.html',
                    {'student': student, 'lessons': search_items}
                )


class StudentEditView(View):
    """Student Edit View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student edit form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                student = get_object_or_404(Student, pk=pk)
                form = AddStudentForm(instance=student)
                return render(
                    request,
                    'students/student_edit.html',
                    {'form': form, 'student': student}
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )

    def post(self, request, pk, *args, **kwargs):
        """Receive student edit form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                student = get_object_or_404(Student, pk=pk)
                form = AddStudentForm(request.POST, instance=student)
                if form.is_valid():
                    print(form.cleaned_data)
                    student = form.save(commit=False)
                    sales_manager = form.cleaned_data['sales_manager'][0]
                    parent = form.cleaned_data['parent'][0]
                    student.save()
                    form.save_m2m()
                    student.sales_manager.add(sales_manager)
                    student.parent.add(parent)
                    student.save()
                    return HttpResponseRedirect(
                        reverse('student_detail', args=[student.pk])
                        )
                return render(
                    request,
                    'students/student_edit.html',
                    {'form': form, 'student': student}
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )


class StudentDeleteView(View):
    """Student Delete View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student delete form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                student = get_object_or_404(Student, pk=pk)
                return render(
                    request,
                    'students/student_delete.html',
                    {'student': student}
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )

    def post(self, request, pk, *args, **kwargs):
        """Receive student delete form"""
        if request.user.is_authenticated:
            if request.user.role == 0 or request.user.role == 2:
                student = get_object_or_404(Student, pk=pk)
                student.delete()
                return HttpResponseRedirect(
                    reverse('students')
                )
            else:
                return render(
                    request,
                    'profiles/access_limitation.html'
                )
