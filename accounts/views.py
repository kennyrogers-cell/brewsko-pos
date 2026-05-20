from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect_by_role(user)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def redirect_by_role(user):
    if user.role == 'admin':
        return redirect('panel:dashboard')
    elif user.role == 'cashier':
        return redirect('cashier:welcome')
    elif user.role == 'kitchen':
        return redirect('kitchen:dashboard')
    return redirect('login')
