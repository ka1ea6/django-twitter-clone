from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Post, User, Profile

# Create your views here.


def index(request):
    return redirect('/home')


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/home/home.html', context={'posts': posts   })

def post(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content is not None:
            profile = Profile.objects.filter(id=3).first()
            post = Post(content=content, profile=profile)
            post.save()

    return redirect('/home')

def explore(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/explore.html', context={'posts': posts   })

def logout(request):
    return render(request, 'core/logout.html')