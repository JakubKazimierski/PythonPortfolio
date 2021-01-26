from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    '''
    View of home page.
    '''
    return HttpResponse('<h1>Blog Home Page</h1>')
    
def about(request):
    '''
    View of description page.
    '''
    return HttpResponse('<h1>Blog About Page</h1>')    