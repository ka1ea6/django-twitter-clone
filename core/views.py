from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Post, User, Profile, Post_Likes
from django.contrib import auth, messages
from datetime import datetime

# Create your views here.


def index(request):
    return redirect('/home')


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    print(request.user)
    user = User.objects.filter(id=request.user.id)

    if request.user is not None or request.user.username != "AnonymousUser":

        profile = Profile.objects.get(user_id=request.user.id)
        return render(request, 'core/home/home.html', context={'posts': posts, 'profile': profile})

    
    return render(request, 'core/home/home.html', context={'posts': posts})

def post(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content is not None:
            profile = Profile.objects.get(user_id=request.user.id)
            post = Post(content=content, profile=profile, created_at=datetime.now())
            post.save()

    return redirect('/home')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'core/login.html')

def explore(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/explore.html', context={'posts': posts   })

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/home')
    return render(request, 'core/logout.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirmPassword']

        if password != password2:
            messages.info(request, "Passwords don't match")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('signup')
        else:
            print('here')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # user_model = User.objects.get(username=username)
            # new_profile = Profile.objects.create(user=user_model, display_name=username)
            # new_profile.save()
            
            auth.login(request, user)
            return redirect('home')
            



    return render(request, 'core/signup.html')

def like_post(request):
    post_id = request.GET.get('post_id')
    profile = Profile.objects.get(user_id=request.user.id)

    like_filter = Post_Likes.objects.filter(post_id=post_id, profile=profile).first()
    print(like_filter)
    if like_filter is None and post_id is not None:
        new_like = Post_Likes.objects.create(post_id=post_id, profile=profile)
        post = Post.objects.get(id=post_id)
        post.like_count += 1
        new_like.save()
        post.save()
    elif like_filter is not None and post_id is not None:
        like_filter.delete()
        post = Post.objects.get(id=post_id)
        post.like_count -= 1
        post.save()
    

    return redirect('home')