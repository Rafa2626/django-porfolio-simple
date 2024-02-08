from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logouts
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserEditForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def editusers(request):
    projects = Project.objects.all()
    return render(request, 'edituser.html')

def hellologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password not correct')
            return render(request, "registration/login.html") 
    else:
        return render(request, "registration/login.html")  


def helloregister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hellologin')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('home')

@login_required
def edituser(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('editusers')
    else:
        form = UserEditForm(instance=request.user)
    
    return render(request, "edituser.html", {'form': form})