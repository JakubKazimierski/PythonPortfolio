'''
Django tests for views.
'''

from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):
    '''
    Class with unittests for views.
    '''
    def setUp(self):
        '''
        Set up for tests.
        '''
        self.client = Client()
        self.form_url = reverse("register")


    def test_home_GET(self):
        '''
        GET method for register test.
        '''

        response = self.client.get(self.form_url)

        self.assertEqual(response.status_code, 200)
        # below looks at dir templates
        self.assertTemplateUsed(response, 'users/register.html')
