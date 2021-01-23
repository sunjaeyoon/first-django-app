from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Event

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all(), #post
        'events': Events.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

