"""View for the home page"""
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')
