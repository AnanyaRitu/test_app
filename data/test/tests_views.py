from django.urls import reverse
from django.test import TestCase, Client
from data.models import *
import json


class TestViews(TestCase):
    def setup(self):
        self.client=Client()
        

    def test_log_in_GET(self):
        response=self.client.get(reverse('log_in'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


    def test_parent_registration_GET(self):
        response=self.client.get(reverse('parent_registration'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'parent_registration.html')


    def test_child_registration_GET(self):
        response=self.client.get(reverse('child_registration'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'child_registration.html')
