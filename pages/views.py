from django.shortcuts import render, get_object_or_404
from django.urls import path
from . import views


def index(request):
    
    context = {}
    return render(request, 'pages/index.html')

