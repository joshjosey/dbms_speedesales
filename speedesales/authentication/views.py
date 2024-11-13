from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django import forms

# Create your views here.
def login_user(request): #handle the user logging in
    #check if they posted the form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have been successfully logged in"))
            return redirect('index')
        else:
            messages.success(request, ("Error please try again"))
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request): #handle the user logging out
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('index')

def register_user(request):
    form = RegistrationForm()

    #if the form has been filled out
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in after registering
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('index')
        else:
            messages.success(request, ("Error registering, try again"))
            return redirect('authentication:register')
    #if the page is being loaded
    return render(request, 'register.html', {'form': form})