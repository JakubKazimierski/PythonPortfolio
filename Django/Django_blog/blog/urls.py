'''
Contains views.
'''

from django.urls import path
from . import views

urlpatterns = [
    # leave empty path for home page
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]