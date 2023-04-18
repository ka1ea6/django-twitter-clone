from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    return redirect('/home')


def home(request):
    return render(request, 'core/home/home.html')
