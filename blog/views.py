from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Jack',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Feb 2, 2025'
    },
    {
        'author': 'Ahmed',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 3, 2025'
    }
]


def home(request):
     blogData = {
          'posts': posts
     }
     return render(request, 'blog/home.html', blogData)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
