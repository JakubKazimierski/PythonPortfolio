from django.test import TestCase
from django.urls import reverse, resolve
from . import views

class TestUrls(TestCase):
    '''
    Django tests for urls views.
    '''

    def test_form_url_resolved(self):
        '''
        Checks if urls are properly resolved.
        '''
        # reverse refers to url by it's name
        url_form = reverse("register")
        
        # resolve() resolve url paths to the corresponding views
        self.assertEqual(resolve(url_form).func, views.register)

