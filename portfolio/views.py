from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def hellologin(request):
    return render(request, "login.html")

def helloregister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hellologin')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})