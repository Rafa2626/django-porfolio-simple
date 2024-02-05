from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def hellologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecciona a una página de éxito.
            return redirect('home')
        else:
            # Agrega un mensaje de error
            messages.error(request, 'Username or password not correct')
            # Redirecciona nuevamente a la página de inicio de sesión
            return redirect('hellologin')
    else:
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

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('home')