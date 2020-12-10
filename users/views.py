from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from news_blog.decorators import anonymous_required
from django.contrib.auth.decorators import login_required


@anonymous_required('main:index')
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = forms.RegisterForm()
    return render(request, 'users/register.html', {'forms': form})


@anonymous_required('main:index')
def login_(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('main:index')

    form = forms.LoginForm()
    return render(request, 'users/login.html', {'forms': form})


@login_required
def logout_(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile(request):
    img = models.Profile.objects.filter(user_id=request.user)
    return render(request, 'users/profile.html', {'i': img})


