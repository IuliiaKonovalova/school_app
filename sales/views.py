from django.shortcuts import render
from django.views import View
from profiles.models import Parent
from .forms import SalesForm
from students.models import Student
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
            sales = Sales.objects.filter(user=request.user)
            return render(
                request,
                'sales/sales_list.html',
                {'sales': sales}
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
            seller = request.user
            buyer = form.cleaned_data['sold_to']
            amount = form.cleaned_data['classes_sold']
            child = form.cleaned_data['sold_to_child']
            student = Student.objects.get(id=child.id)
            student.classes_left += amount
            student.save()
            new_sale = Sales.objects.create(
                sold_by=seller,
                sold_to=buyer,
                amount=amount,
            )
            new_sale.save()
            return HttpResponseRedirect()


