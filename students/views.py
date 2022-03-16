"""Views for the students app."""
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Student
from lessons.models import Lesson
from .forms import AddStudentForm


class StudentAddView(View):
    """Student Add View"""
    def get(self, request):
        """Receive student add form"""
        form = AddStudentForm()
        # form.fields['student'].queryset = Student.objects.all()
        return render(
            request,
            'students/student_add.html',
            {'form': form}
            )

    def post(self, request):
        """Receive student add form"""
        form = AddStudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            student = form.save(commit=False)
            sales_manager= form.cleaned_data['sales_manager'][0]
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


class StudentsView(View):
    """Students View"""
    def get(self, request, *args, **kwargs):
        """Receive students list"""
        students = Student.objects.all()
        return render(
            request,
            'students/students.html',
            {'students': students}
            )


class StudentView(View):
    """Student View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student detail"""
        student = get_object_or_404(Student, pk=pk)
        lessons = Lesson.objects.filter(students__in=[student])
        return render(
            request,
            'students/student_detail.html',
            {'student': student, 'lessons': lessons}
            )


class StudentEditView(View):
    """Student Edit View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student edit form"""
        student = get_object_or_404(Student, pk=pk)
        form = AddStudentForm(instance=student)
        return render(
            request,
            'students/student_edit.html',
            {'form': form, 'student': student}
            )

    def post(self, request, pk, *args, **kwargs):
        """Receive student edit form"""
        student = get_object_or_404(Student, pk=pk)
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            print(form.cleaned_data)
            student = form.save(commit=False)
            sales_manager= form.cleaned_data['sales_manager'][0]
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


class StudentDeleteView(View):
    """Student Delete View"""
    def get(self, request, pk, *args, **kwargs):
        """Receive student delete form"""
        student = get_object_or_404(Student, pk=pk)
        return render(
            request,
            'students/student_delete.html',
            {'student': student}
            )

    def post(self, request, pk, *args, **kwargs):
        """Receive student delete form"""
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return HttpResponseRedirect(
            reverse('students')
            )
