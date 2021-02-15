from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # app/model_viewtype.html
    context_object_name = 'posts'
    oredering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

def about(request):
    '''
    View of description page.
    '''
    return render(request, 'blog/about.html', {'title' : 'Description Site'})