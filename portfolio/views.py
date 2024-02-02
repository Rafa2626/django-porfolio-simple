from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def hellologin(request):
    return render(request, "login.html")

def helloregister(request):
    return render(request, "register.html")



@login_required
def products(request):
    return render(request, 'templates/index.html')

#def register(request):
#    data = {
#        'form': CustomUserCreationForm()
#    }
#
#    if request.method == 'POST':
#        user_creation_form = CustomUserCreationForm(data=request.POST)
#
#        if user_creation_form.is_valid():
#            user_creation_form.save()

#            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
#            login(request, user)
#            return redirect('index.html')
#        else:
#            data['form'] = user_creation_form
#
#    return render(request, "register.html", data)
