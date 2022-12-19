"""Views for the sales app."""
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
from profiles.models import Parent, SalesManager
from students.models import Student
from .forms import SalesForm
from .models import Sales


class SalesView(View):
    """Sales view"""
    def get(self, request, *args, **kwargs):
        """Receive sales"""
        if request.user.is_authenticated and (
            request.user.role == 0 or request.user.role == 2
        ):
            if Sales.objects.all().count() > 0:
                p = Paginator(Sales.objects.all(), 10)
                page = request.GET.get('page')
                sales = p.get_page(page)
                for sale in sales:
                    student = Student.objects.get(id=sale.student_id)
                    sale.student_name = (
                        student.first_name +
                        ' ' +
                        student.last_name
                    )
                    sales_number = Sales.objects.all().count()
                return render(
                    request,
                    'sales/sales_list.html',
                    {'sales': sales, 'sales_number': sales_number}
                    )
            return render(
                request,
                'sales/sales_list.html',
                {'sales': sales}
                )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )

    def post(self, request, *args, **kwargs):
        """Search by date"""
        if request.user.is_authenticated and (
            request.user.role == 0 or request.user.role == 2
        ):
            fromdate = request.POST.get('from_date')
            todate = request.POST.get('to_date')
            p = Paginator(
                Sales.objects.filter(date__range=[fromdate, todate]),
                10
            )
            page = request.GET.get('page')
            search_items = p.get_page(page)
            sales_number = Sales.objects.filter(
                date__range=[fromdate, todate]
            ).count()
            return render(
                request,
                'sales/sales_list.html',
                {'sales': search_items, 'sales_number': sales_number}
            )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )


def sales_form(request):
    """Sales form"""
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.role == 2:
            form = SalesForm()
            form.fields['sold_to'].queryset = Parent.objects.all()
            form.fields['student'].queryset = Student.objects.all()
            return render(
                request,
                'sales/sales_form.html',
                {'form': form}
            )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )

    if request.method == "POST":
        if request.user.is_authenticated and request.user.role == 2:
            form = SalesForm(request.POST)
            if form.is_valid():
                seller = SalesManager.objects.get(user=request.user)
                buyer = form.cleaned_data['sold_to']
                amount = form.cleaned_data['amount']
                child = form.cleaned_data['student']
                student = Student.objects.get(id=child.id)
                student.classes_left += amount
                student.save()
                seller.total_sold += amount
                seller.save()
                new_sale = Sales.objects.create(
                    sold_by=seller,
                    sold_to=buyer,
                    amount=amount,
                    student_id=child.id
                )
                new_sale.save()
                return HttpResponseRedirect(
                    reverse('sales_list')
                )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )


def edit_sales(request, pk):
    """Edit sales"""
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.role == 2:
            sales = Sales.objects.get(id=pk)
            form = SalesForm(instance=sales)
            form.fields['sold_to'].queryset = Parent.objects.all()
            form.fields['student'].queryset = Student.objects.all()
            student = Student.objects.get(id=sales.student_id)
            form.fields['student'].initial = student
            amount_of_classes = sales.amount
            return render(
                request,
                'sales/edit_sales.html',
                {'form': form}
                )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )
    if request.method == "POST":
        if request.user.is_authenticated and request.user.role == 2:
            sales = Sales.objects.get(id=pk)
            student = Student.objects.get(id=sales.student_id)
            amount_of_classes = sales.amount
            student.classes_left -= amount_of_classes
            student.save()
            seller = SalesManager.objects.get(user=request.user)
            seller.total_sold -= amount_of_classes
            seller.save()
            form = SalesForm(request.POST, instance=sales)
            if form.is_valid():
                seller = SalesManager.objects.get(user=request.user)
                buyer = form.cleaned_data['sold_to']
                amount = form.cleaned_data['amount']
                child = form.cleaned_data['student']
                student = Student.objects.get(id=child.id)
                student.classes_left += amount
                student.save()
                seller.total_sold += amount
                seller.save()
                sales.sold_by = seller
                sales.sold_to = buyer
                sales.amount = amount
                sales.student_id = child.id
                sales.save()
                return HttpResponseRedirect(
                    reverse('sales_list')
                )
            else:
                return render(
                    request,
                    'sales/edit_sales.html',
                    {'form': form}
                )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )


def delete_sales(request, pk):
    """Delete sales"""
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.role == 2:
            sales = Sales.objects.get(id=pk)
            student = Student.objects.get(id=sales.student_id)
            return render(
                request,
                'sales/delete_sales.html',
                {'sales': sales, 'student': student}
                )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )

    if request.method == "POST":
        if request.user.is_authenticated and request.user.role == 2:
            sales = Sales.objects.get(id=pk)
            student = Student.objects.get(id=sales.student_id)
            amount_of_classes = sales.amount
            student.classes_left -= amount_of_classes
            student.save()
            seller = SalesManager.objects.get(user=request.user)
            seller.total_sold -= amount_of_classes
            seller.save()
            sales.delete()
            return HttpResponseRedirect(
                reverse('sales_list')
            )
        else:
            return render(
                request,
                'profiles/access_limitation.html'
            )
