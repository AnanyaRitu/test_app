from django.test import SimpleTestCase
from django.urls import reverse, resolve
from data.views import *

class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url=reverse('log_in')
        self.assertEquals(resolve(url).func, log_in)

    def test_logout_url_is_resolved(self):
        url=reverse('log_out')
        self.assertEquals(resolve(url).func, log_out)

    def test_parent_registration_url_is_resolved(self):
        url=reverse('parent_registration')
        self.assertEquals(resolve(url).func, parent_registration)

    def test_child_registration_url_is_resolved(self):
        url=reverse('child_registration')
        self.assertEquals(resolve(url).func, child_registration)

    def test_parent_home_url_is_resolved(self):
        url=reverse('parent_home')
        self.assertEquals(resolve(url).func, parent_home)
    
    def test_parent_create_data_view_url_is_resolved(self):
        url=reverse('parent_create_data_view')
        self.assertEquals(resolve(url).func, parent_create_data_view)

    def test_parent_update_data_view_url_is_resolved(self):
        url=reverse('parent_update_data_view')
        self.assertEquals(resolve(url).func, parent_update_data_view)

    def test_child_home_url_is_resolved(self):
        url=reverse('child_home')
        self.assertEquals(resolve(url).func, child_home)
    
    def test_child_create_data_view_url_is_resolved(self):
        url=reverse('child_create_data_view')
        self.assertEquals(resolve(url).func, child_create_data_view)

    def test_child_update_data_view_url_is_resolved(self):
        url=reverse('child_update_data_view')
        self.assertEquals(resolve(url).func, child_update_data_view)


    def test_parent_username_list_url_is_resolved(self):
        url=reverse('parent_username_list')
        self.assertEquals(resolve(url).func, parent_username_list)

    def test_parent_data_create_url_is_resolved(self):
        url=reverse('parent_data_create', args=['anything'])
        self.assertEquals(resolve(url).func, parent_data_create)
    
    def test_parent_data_update_url_is_resolved(self):
        url=reverse('parent_data_update', args=['anything'])
        self.assertEquals(resolve(url).func, parent_data_update)

    def test_parent_data_delete_url_is_resolved(self):
        url=reverse('parent_data_delete', args=['anything'])
        self.assertEquals(resolve(url).func, parent_data_delete)


    def test_child_username_list_url_is_resolved(self):
        url=reverse('child_username_list')
        self.assertEquals(resolve(url).func, child_username_list)

    def test_child_data_create_url_is_resolved(self):
        url=reverse('child_data_create', args=['anything'])
        self.assertEquals(resolve(url).func, child_data_create)
    
    def test_child_data_update_url_is_resolved(self):
        url=reverse('child_data_update', args=['anything'])
        self.assertEquals(resolve(url).func, child_data_update)

    def test_child_data_delete_url_is_resolved(self):
        url=reverse('child_data_delete', args=['anything'])
        self.assertEquals(resolve(url).func, child_data_delete)

    