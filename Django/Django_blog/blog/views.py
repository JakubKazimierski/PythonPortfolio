from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    '''
    View of home page.
    '''

    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html', context)
    
def about(request):
    '''
    View of description page.
    '''
    return render(request, 'blog/about.html', {'title' : 'Description Site'})