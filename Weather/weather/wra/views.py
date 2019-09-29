from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'wra/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'wra/about.html', {'title': 'About'})


