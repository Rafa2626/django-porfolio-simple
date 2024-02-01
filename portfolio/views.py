from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def hellologin(request):
    return render(request, "login.html")