from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, ChangePasswordForm, ChangeEmailForm
from django.contrib.auth.models import User

def login_user(request): # cannot be named login because we are importing it
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ('error logging in'))
            return redirect('login')
    return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'bye')
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("registration successful"))
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register_user.html', {'form': form})

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password updated, yay!')
                return redirect('index')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'membership/update_password.html', {'form': form})
    else:
        return redirect('index') # If user is not logged in
    
def update_email(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = ChangeEmailForm(instance=current_user)
        if request.method == "POST":
            form = ChangeEmailForm(request.POST or None, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Email has been updated')
                return redirect('dashboard')
            else:
                messages.success(request, 'We encountered an error')
    return render(request, 'membership/update_email.html', {'form': form})