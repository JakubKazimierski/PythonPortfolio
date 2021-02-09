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


    def test_GET_register(self):
        '''
        GET method for register, tests.
        '''
        response = self.client.get(self.form_url)

        self.assertEqual(response.status_code, 200)
        # below looks at dir templates
        self.assertTemplateUsed(response, 'users/register.html')

    def test_POST_register(self):
        '''
        POST method for register, tests.
        '''

        response = self.client.post(self.form_url, {
             'username' : 'TestsUSers', 
             'email' : 'email@is.ok',
             'password1' : 'Testtest321',
             'password2' : 'Testtest321',

        })

        self.assertEqual(response.status_code, 302)
