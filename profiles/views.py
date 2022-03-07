from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import NewApplicationForm


class UserProfileView(View):
    """User Profile"""
    def get(self, request, phone, *args, **kwargs):
        """Receive user profile"""
        user_profile = get_object_or_404(CustomUser, phone=phone)
        # if request.user.is_authenticated:
        #     if request.user == user_profile:
        #         form = PasswordChangeForm(request.user)
        #         form.fields['old_password'].widget.attrs['autofocus'] = False
        #         return render(
        #             request,
        #             'profiles/user_profile.html',
        #             {'user_profile': user_profile, 'password_form': form}
        #             )
        return render(
            request,
            'profiles/user_profile.html',
            {'user_profile': user_profile}
            )

    # def post(self, request, phone, *args, **kwargs):
    #     """Updating password"""
    #     user_profile = get_object_or_404(CustomUser, phone=phone)
    #     if request.user.is_authenticated:
    #         if request.user == user_profile:
    #             form = PasswordChangeForm(request.user, request.POST)
    #             if form.is_valid():
    #                 user = form.save()
    #                 update_session_auth_hash(request, user)
    #                 return HttpResponseRedirect(
    #                     reverse(
    #                         'user_profile',
    #                         kwargs={'phone': user_profile.phone})
    #                         )
    #             else:
    #                 return render(
    #                     request,
    #                     'profiles/user_profile.html',
    #                     {'user_profile': user_profile, 'password_form': form}
    #                     )
    #     return render(
    #         request,
    #         'profiles/user_profile.html',
    #         {'user_profile': user_profile}
    #         )


# Add UserProfileEditView to change user profile phone, first_name, last_name
class UserProfileEditView(View):
    """
    Edit user profile
    """
    def get(self, request, phone, *args, **kwargs):
        """Receive user profile"""
        user_profile = get_object_or_404(CustomUser, phone=phone)
        if request.user.is_authenticated:
            if request.user == user_profile:
                form = PasswordChangeForm(request.user)
                form.fields['old_password'].widget.attrs['autofocus'] = False
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

    def post(self, request, phone, *args, **kwargs):
        """Update user profile"""
        user_profile = get_object_or_404(CustomUser, phone=phone)
        if request.user.is_authenticated:
            if request.user == user_profile:
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return HttpResponseRedirect(
                        reverse(
                            'user_profile',
                            kwargs={'phone': user_profile.phone})
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
        new_applications = CustomUser.objects.filter(role=6)
        return render(
            request,
            'profiles/new_applications.html',
            {'new_applications': new_applications}
            )


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
            new_application = form.save()
            return HttpResponseRedirect(
                reverse(
                    'application_detail',
                    args=[request.user.phone, new_application.pk]
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
                    args=[request.user.phone, new_application.pk]
                    )
                    )
    def post(self, request, pk, *args, **kwargs):
        """Delete new applications"""
        new_application = get_object_or_404(CustomUser, pk=pk)
        new_application.delete()
        return HttpResponseRedirect(
            reverse(
                'new_applications',
                args=[request.user.phone]
                    )
                    )

# SearchMembersView to sort all members by role
class SearchMembersView(View):
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
