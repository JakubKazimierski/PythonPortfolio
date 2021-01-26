from django.test import TestCase
from django.urls import reverse, resolve
from . import views

class TestUrls(TestCase):
    '''
    Django tests for urls views.
    '''

    def test_home_url_resolved(self):
        '''
        Checks if urls are properly resolved.
        '''
        # reverse refers to url by it's name
        url_home = reverse("blog-home")
        
        # resolve() resolve url paths to the corresponding views
        self.assertEqual(resolve(url_home).func, views.home)

    def test_about_url_resolved(self):
        '''
        Checks if urls are properly resolved.
        '''
        url_about = reverse("blog-about")
        
        self.assertEqual(resolve(url_about).func, views.about)
