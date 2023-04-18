from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Post, User

# Create your views here.


def index(request):
    return redirect('/home')


def home(request):
    return render(request, 'core/home/home.html')

def post(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content is not None:
            user = User.objects.filter(id=1).first()
            post = Post(content=content, user=user)
            post.save()

    return redirect('/home')
