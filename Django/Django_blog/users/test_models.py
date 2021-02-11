from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from .signals import create_profile

class TestModels(TestCase):
    '''
    Django tests for models.
    '''

    def setUp(self):
        '''
        Sets up new profile.
        '''
        self.user = User(username='NewUser')
        try:
            post_save.connect(create_profile, sender=self.user)
        except:
            return "Error creating profile"    

    def test_new_profile(self):
        '''
        Checks if profile is created.
        '''
        # resolve() resolve url paths to the corresponding views
        self.assertEqual(self.setUp(), None)

