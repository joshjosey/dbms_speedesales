from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, UpdateForm, UpdateCustomerForm
from .models import Customer
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

def update_user(request):
    if request.user.is_authenticated:
        #get the user table instance
        cur_user = User.objects.get(id=request.user.id)
        
        #check if the user is a customer or employee
        if not cur_user.is_staff:
            #get the customer table instance
            cur_customer = Customer.objects.get(user=cur_user)
        else:
            cur_customer = cur_user
        #get the two forms
        update_form = UpdateForm(request.POST or None, instance=cur_user)
        update_customer_form = UpdateCustomerForm(request.POST or None, instance=cur_customer)
        if update_form.is_valid() and update_customer_form.is_valid():
            update_form.save()
            update_customer_form.save()
            login(request, cur_user)
            messages.success(request, "Account has been updated")
            return redirect('index')
        
        return render(request, "update.html", {'update_form':update_form,'update_customer_form':update_customer_form,})
    else:
        return redirect('authentication:login')
