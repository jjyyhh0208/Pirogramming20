from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def main (request):
    return render(request, 'users/main.html')

def user_signup (request):
    if request.method == 'GET':
        form = UserSignUp()
        ctx = {
            'form' : form
        }
        return render(request, 'users/user_signup.html', ctx)
    else:
        form=UserSignUp(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users:login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:main')
        else:
            ctx = {'form': form, 'error_message': '다시 확인해주세요'}
            return render(request, 'users/user_login.html', ctx)
    else:
        form = AuthenticationForm()

        ctx = {
            'form' : form
        }
        return render(request, 'users/user_login.html', ctx)

def user_logout(request):
    logout(request)
    return render(request, 'users/main.html')

def user_update(request):
    user = request.user
    form = UserUpdate(instance = user)
    if request.method == 'POST':
        form = UserUpdate(request.POST, instance = user)
        if form.is_valid():
            form.save()
        return redirect('users:detail')
    return render(request, 'users/user_update.html', {'form' : form})

def user_detail(request):
    user = request.user
    ctx = {
        'user' : user
    }
    return render(request, 'users/user_detail.html', ctx)

def user_delete(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
    return redirect('users:main')