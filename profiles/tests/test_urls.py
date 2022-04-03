"""Test Profiles URLs."""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import (
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


class TestUrls(SimpleTestCase):
    """Test the urls for the profiles app."""
    def test_user_profile_url(self):
        """Test the user_profile url."""
        url = reverse('user_profile', args=['username'])
        self.assertEqual(resolve(url).func.view_class, UserProfileView)

    def test_user_profile_edit_url(self):
        """Test the user_profile_edit url."""
        url = reverse('user_profile_edit', args=['username'])
        self.assertEqual(resolve(url).func.view_class, UserProfileEditView)

    def test_user_profile_edit_password_url(self):
        """Test the user_profile_edit_password url."""
        url = reverse('user_profile_change_password', args=['username'])
        self.assertEqual(
            resolve(url).func.view_class,
            UserProfileEditPasswordView
        )

    def test_new_applications_url(self):
        """Test the new_applications url."""
        url = reverse('new_applications', args=['username'])
        self.assertEqual(resolve(url).func.view_class, NewApplicationsView)

    def test_new_applications_detail_url(self):
        """Test the new_applications_detail url."""
        url = reverse('application_detail', args=['username', '1'])
        self.assertEqual(
            resolve(url).func.view_class,
            NewApplicationsDetailView
        )

    def test_new_applications_delete_url(self):
        """Test the new_applications_delete url."""
        url = reverse('application_delete', args=['username', '1'])
        self.assertEqual(
            resolve(url).func.view_class,
            NewApplicationsDeleteView
        )

    def test_search_members_url(self):
        """Test the search_members url."""
        url = reverse('search_members', args=['username'])
        self.assertEqual(resolve(url).func.view_class, SearchMembersView)

    def test_delete_member_url(self):
        """Test the delete_member url."""
        url = reverse('delete_member', args=['username'])
        self.assertEqual(resolve(url).func.view_class, DeleteMemberView)

    def test_add_relation_to_parent_url(self):
        """Test the add_relation_to_parent url."""
        url = reverse('add_relation')
        self.assertEqual(resolve(url).func.view_class, AddRelationToParentView)
        url = reverse('add_relation')
        self.assertEqual(resolve(url).func.view_class, AddRelationToParentView)
