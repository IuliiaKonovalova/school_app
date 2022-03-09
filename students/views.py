from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from .models import Student
from .forms import AddStudentForm
from django.http import HttpResponseRedirect




class StudentAddView(View):
    """Student Add View"""
    def get(self, request):
        """Receive student add form"""
        form = AddStudentForm()
        return render(
            request,
            'students/student_add.html',
            {'form': form}
            )

    def post(self, request):
        """Receive student add form"""
        form = AddStudentForm(request.POST)
        if form.is_valid():
            # when saving a student need to exclude relation field from the form
            student = form.save(commit=False).exclude(parent_relation='')
            form.save_m2m()
            student.parent.add(request.user)
            student.parent.relation = form['parent_relation'].value()
            student.sales_manager.add(request.user)
            student.save()
            return HttpResponseRedirect(
                reverse('student_list')
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
        return render(
            request,
            'students/student_detail.html',
            {'student': student}
            )
