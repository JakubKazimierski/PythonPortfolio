from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'Jakub Kazimierski',
        'title' : 'First post',
        'content' : 'First tweet',
        'date_posted' : 'January 28 2021',
    
    },
    {
        'author' : 'Jakub Kazimierski',
        'title' : 'Second post',
        'content' : 'Second tweet',
        'date_posted' : 'January 28 2021',
    
    }

]


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