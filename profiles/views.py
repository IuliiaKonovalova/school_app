from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from students.models import Student
from .models import CustomUser, Parent, SalesManager
from sales.models import Sales
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import NewApplicationForm, UserProfileEditForm


class UserProfileView(View):
    """User Profile"""
    def get(self, request, *args, **kwargs):
        """Receive user profile"""
        user_profile = get_object_or_404(CustomUser,  username=kwargs['username'])
        if user_profile.role == 4:
            children = Student.objects.filter(parent__user=user_profile)
            return render(
                request,
                'profiles/user_profile.html',
                {'user_profile': user_profile, 'children': children}
                )
        if user_profile.role == 2:
            sales_manager = SalesManager.objects.get(user=user_profile)
            children = Student.objects.filter(sales_manager__user=user_profile)
            # sales = Sales.objects.filter(sold_by=sales_manager)
            sales = Sales.objects.all()
            return render(
                request,
                'profiles/user_profile.html',
                {
                    'user_profile': user_profile,
                    'sales': sales,
                    'children': children
                }
                )
        return render(
            request,
            'profiles/user_profile.html',
            {'user_profile': user_profile}
            )


class UserProfileEditView(View):
    """User Profile Edit"""
    def get(self, request, *args, **kwargs):
        """Receive user profile edit form"""
        user_profile = get_object_or_404(CustomUser, username=kwargs['username'])
        form = UserProfileEditForm(instance=user_profile)
        form.fields['role'].initial = request.user.role
        return render(
            request,
            'profiles/user_profile_edit.html',
            {'user_profile': user_profile, 'form': form}
            )

    def post(self, request, *args, **kwargs):
        """Receive user profile edit form"""
        user_profile = get_object_or_404(CustomUser, username=kwargs['username'])
        if request.user.is_authenticated:
            if request.user == user_profile:
                form = UserProfileEditForm(request.POST, instance=user_profile)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(
                        reverse(
                            'user_profile',
                            kwargs={'username': user_profile.username})
                            )
                else:
                    print('form is not valid')
        return render(
            request,
            'profiles/user_profile_edit.html',
            {'user_profile': user_profile, 'form': form}
            )


class UserProfileEditPasswordView(View):
    """
    Edit user profile
    """
    def get(self, request, *args, **kwargs):
        """Receive user profile"""
        user_profile = get_object_or_404(CustomUser, username=kwargs['username'])
        if request.user.is_authenticated:
            if request.user == user_profile:
                form = PasswordChangeForm(request.user)
                form.fields['old_password'].widget.attrs['autofocus'] = False
                return render(
                    request,
                    'profiles/user_profile_change_password.html',
                    {'user_profile': user_profile, 'password_form': form}
                    )
        return render(
            request,
            'profiles/user_profile_change_password.html',
            {'user_profile': user_profile}
            )

    def post(self, request, *args, **kwargs):
        """Update user profile"""
        user_profile = get_object_or_404(CustomUser, username=kwargs['username'])
        if request.user.is_authenticated:
            if request.user == user_profile:
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return HttpResponseRedirect(
                        reverse(
                            'user_profile',
                            kwargs={'username': user_profile.username})
                            )
                else:
                    return render(
                        request,
                        'profiles/user_profile_edit.html',
                        {'user_profile': user_profile, 'password_form': form}
                        )
        return render(
            request,
            'profiles/user_profile_edit.html',
            {'user_profile': user_profile}
            )


class NewApplicationsView(View):
    """New Applications"""
    def get(self, request, *args, **kwargs):
        """Receive new applications"""
        new_applications = CustomUser.objects.filter(role=5)
        return render(request, 'profiles/new_applications.html', {'new_applications': new_applications})


class NewApplicationsDetailView(View):
    """New Applications Detail"""
    def get(self, request, pk, *args, **kwargs):
        """Receive new applications"""
        new_application = get_object_or_404(CustomUser, pk=pk)
        form = NewApplicationForm(instance=new_application)
        if request.user.is_authenticated:
            if request.user.role == 0:
                return render(
                    request,
                    'profiles/application_detail.html',
                    {'new_application': new_application, 'form': form}
                    )
        return render(
            request,
            'profiles/application_detail.html',
            {'new_application': new_application,}
            )
    def post(self, request, pk, *args, **kwargs):
        """Update new applications"""
        new_application = get_object_or_404(CustomUser, pk=pk)
        form = NewApplicationForm(request.POST, instance=new_application)
        if form.is_valid():
            new_application = form.save(commit=False)
            if new_application.role == 4:
                new_parent = Parent.objects.create(
                    user=new_application,
                )
                new_parent.save()
            if new_application.role == 2:
                new_parent = SalesManager.objects.create(
                    user=new_application,
                )
                new_parent.save()
            new_application.save()
            return HttpResponseRedirect(
                reverse(
                    'application_detail',
                    args=[request.user.username, new_application.pk]
                    )
                )
        return render(
            request,
            'profiles/application_detail.html',
            {'new_application': new_application, 'form': form}
            )


class NewApplicationsDeleteView(View):
    """New Applications Delete"""
    def get(self, request, pk, *args, **kwargs):
        """Receive new applications"""
        new_application = get_object_or_404(CustomUser, pk=pk)
        if request.user.is_authenticated:
            if request.user.role == 0:
                return render(
                    request,
                    'profiles/application_delete.html',
                    {'new_application': new_application}
                    )
        else:
            return HttpResponseRedirect(
                reverse(
                    'application_detail',
                    args=[request.user.username, new_application.pk]
                    )
                    )
    def post(self, request, pk, *args, **kwargs):
        """Delete new applications"""
        new_application = get_object_or_404(CustomUser, pk=pk)
        new_application.delete()
        return HttpResponseRedirect(
            reverse(
                'new_applications',
                args=[request.user.username]
                    )
                    )

class SearchMembersView(ListView):
    """Search Members"""
    def get(self, request, *args, **kwargs):
        """Receive members"""
        members = CustomUser.objects.all()
        if request.user.is_authenticated:
            if request.user.role != 5 and request.user.role != 6:
                return render(
                    request,
                    'profiles/search_members.html',
                    {'members': members}
                    )
