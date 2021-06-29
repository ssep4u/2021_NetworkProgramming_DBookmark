from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return render(request, 'accounts/register_done.html', {'profile': profile})  # redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bookmark:list')
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def my_logout(request):
    logout(request)
    return redirect('bookmark:list')
