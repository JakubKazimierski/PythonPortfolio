from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Jakub K',
        'title' : 'First post',
        'content' : 'First content',
        'date_posted' : 'January 28 2021',
    
    },
    {
        'author' : 'Jakub K',
        'title' : 'Second post',
        'content' : 'Second content',
        'date_posted' : 'January 28 2021',
    
    }

]


def home(request):
    '''
    View of home page.
    '''

    context = {
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)
    
def about(request):
    '''
    View of description page.
    '''
    return render(request, 'blog/about.html')