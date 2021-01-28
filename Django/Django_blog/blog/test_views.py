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
        self.home_url = reverse("blog-home")
        self.about_url = reverse("blog-about")


    def test_home_GET(self):
        '''
        GET method for blog-home test.
        '''

        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        # below looks at dir templates
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_about_GET(self):
        '''
        GET method for blog-about test.
        '''

        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')