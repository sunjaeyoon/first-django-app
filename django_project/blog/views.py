from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
post =[
    {
        'author':'Hello',
        'title':'Heyyyyy',
        'content':'Whats Up',
        'date_posted':'August 20, 2021'
    },
    {
        'author':'Hello',
        'title':'Heyyyyy',
        'content':'Whats Up',
        'date_posted':'August 20, 2021'
    },
    {
        'author':'Hello',
        'title':'Heyyyyy',
        'content':'Whats Up',
        'date_posted':'August 20, 2021'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

