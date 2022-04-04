"""Tests for the sales urls app."""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from sales.views import (
    SalesView, sales_form, edit_sales, delete_sales
)


class TestUrls(SimpleTestCase):
    """Test the urls for the sales app."""

    def test_sales_url_resolves(self):
        """Test the sales url resolves."""
        url = reverse('sales_list')
        self.assertEquals(resolve(url).func.view_class, SalesView)

    def test_sales_form_url_resolves(self):
        """Test the sales form url resolves."""
        url = reverse('sales_form')
        self.assertEquals(resolve(url).func, sales_form)

    def test_edit_sales_url_resolves(self):
        """Test the edit sales url resolves."""
        url = reverse('edit_sales', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, edit_sales)

    def test_delete_sales_url_resolves(self):
        """Test the delete sales url resolves."""
        url = reverse('delete_sales', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, delete_sales)
