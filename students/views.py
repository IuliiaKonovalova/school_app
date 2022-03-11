from django.shortcuts import render, get_object_or_404, reverse
from django.views import View

from profiles.models import CustomUser, SalesManager
from .models import Student
from .forms import AddStudentForm
from django.http import HttpResponseRedirect




class StudentAddView(View):
    """Student Add View"""
    def get(self, request):
        """Receive student add form"""
        form = AddStudentForm()
        # form.fields['sales_manager'].queryset = CustomUser.objects.filter(role=2)
        # form.fields['parent'].queryset = CustomUser.objects.filter(role=4)
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
            # when saving a student need to exclude relation field from the form
            student = form.save(commit=False)
            sales_manager= form.cleaned_data['sales_manager'][0]
            # sales_manager = get_object_or_404(CustomUser, pk=sales_manager_id)
            parent = form.cleaned_data['parent'][0]
            # parent = get_object_or_404(CustomUser, pk=parent_id)
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
        return render(
            request,
            'students/student_detail.html',
            {'student': student}
            )
