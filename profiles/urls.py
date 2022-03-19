"""Urls for the profiles app."""
from django.urls import path
from .views import (
    UserProfileView,
    UserProfileEditView,
    UserProfileEditPasswordView,
    NewApplicationsView,
    NewApplicationsDetailView,
    NewApplicationsDeleteView,
    SearchMembersView,
    DeleteMemberView,
    AddRelationToParentView,
    )


urlpatterns = [
    path(
        '<username>/',
        UserProfileView.as_view(),
        name='user_profile'
    ),
    path(
        '<username>/search/',
        SearchMembersView.as_view(),
        name='search_members'
    ),
    path(
        '<username>/edit/',
        UserProfileEditView.as_view(),
        name='user_profile_edit'
    ),
    path(
        '<username>/change/',
        UserProfileEditPasswordView.as_view(),
        name='user_profile_change_password'
    ),
    path(
        '<username>/applications/',
        NewApplicationsView.as_view(),
        name='new_applications'
    ),
    path(
        '<username>/applications/<int:pk>/',
        NewApplicationsDetailView.as_view(),
        name='application_detail'
    ),
    path(
        '<username>/applications/<int:pk>/delete/',
        NewApplicationsDeleteView.as_view(),
        name='application_delete'
    ),
    path(
        '<username>/delete/',
        DeleteMemberView.as_view(),
        name='delete_member'
    ),
    path(
        '',
        AddRelationToParentView.as_view(),
        name='add_relation'
    ),
]
