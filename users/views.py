from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username OR Password is incorrect!!')
            
    return render(request, 'login.html', {'loginform': form})

def logoutUser(request):
    logout(request)
    messages.info(request, 'User successfully Logged out')
    return redirect('login')
    
def userRegistration(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user =form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created successfully')
            
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'An error has occured during registration') 
        
    return render(request, 'profiles.html', {'form': form})