from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View
from secretstorage import search_items
from profiles.models import Parent, SalesManager
from students.models import Student
from .forms import SalesForm
from .models import Sales


# Add class to view all sales for a user with role 0 or 2
class SalesView(View):
    """Sales view"""
    def get(self, request, *args, **kwargs):
        """Receive sales"""
        if request.user.is_authenticated and request.user.role == 0:
            sales = Sales.objects.all()
            return render(
                request,
                'sales/sales_list.html',
                {'sales': sales}
                )
        if request.user.is_authenticated and request.user.role == 2:
            sales_manager = SalesManager.objects.get(user=request.user)
            sales = Sales.objects.filter(sold_by=sales_manager)
            return render(
                request,
                'sales/sales_list.html',
                {'sales': sales}
                )

    def post(self, request, *args, **kwargs):
        """Search by date"""
        if request.user.is_authenticated and (request.user.role == 0 or request.user.role == 2):
            fromdate=request.POST.get('from_date')
            todate=request.POST.get('to_date')
            search_items=Sales.objects.raw("SELECT * FROM sales WHERE date BETWEEN %s AND %s",[fromdate,todate])
            return render(
                request,
                'sales/sales_list.html',
                {'sales': search_items}
                )



def sales_form(request):
    """Sales form"""
    if request.method == 'GET':
        if request.user.is_authenticated and (request.user.role == 0 or request.user.role == 2):
            form = SalesForm()
            form.fields['sold_to'].queryset = Parent.objects.all()
            form.fields['student'].queryset = Student.objects.all()
            return render(
                request,
                'sales/sales_form.html',
                {'form': form}
                )
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            seller = SalesManager.objects.get(user=request.user)
            buyer = form.cleaned_data['sold_to']
            amount = form.cleaned_data['amount']
            child = form.cleaned_data['student']
            student = Student.objects.get(id=child.id)
            student.classes_left += amount
            student.save()
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


# Add edit sales for a user with role 0 or 2
def edit_sales(request, pk):
    """Edit sales"""
    # amount_of_classes = 0
    if request.method == 'GET':
        if request.user.is_authenticated and (
            request.user.role == 0 or request.user.role == 2
        ):
            sales = Sales.objects.get(id=pk)
            form = SalesForm(instance=sales)
            form.fields['sold_to'].queryset = Parent.objects.all()
            form.fields['student'].queryset = Student.objects.all()
            student = Student.objects.get(id=sales.student_id)
            # student should be selected in the form
            form.fields['student'].initial = student
            amount_of_classes = sales.amount
            return render(
                request,
                'sales/edit_sales.html',
                {'form': form}
                )
    if request.method == "POST":
        sales = Sales.objects.get(id=pk)
        student = Student.objects.get(id=sales.student_id)
        amount_of_classes = sales.amount
        student.classes_left -= amount_of_classes
        student.save()
        form = SalesForm(request.POST, instance=sales)
        if form.is_valid():
            seller = SalesManager.objects.get(user=request.user)
            buyer = form.cleaned_data['sold_to']
            amount = form.cleaned_data['amount']
            child = form.cleaned_data['student']
            student = Student.objects.get(id=child.id)
            student.classes_left += amount
            student.save()
            sales.sold_by = seller
            sales.sold_to = buyer
            sales.amount = amount
            sales.student_id = child.id
            sales.save()
            return HttpResponseRedirect(
                reverse('sales_list')
            )