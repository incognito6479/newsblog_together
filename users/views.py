from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm, ProfilePicsForm, LoginForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from news_blog.decorators import anonymous_required
from django.contrib.auth.decorators import login_required
from main.models import Posts


@anonymous_required('main:index')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            profile_ = Profile(image='static/default.png', user_id=user.id)
            profile_.save()
            return redirect('login')

    form = RegisterForm()
    return render(request, 'users/register.html', {'forms': form})


@anonymous_required('main:index')
def login_(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('main:index')

    form = LoginForm()
    return render(request, 'users/login.html', {'forms': form})


@login_required
def logout_(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile(request):
    img = Profile.objects.filter(user_id=request.user)
    posts_user = Posts.objects.filter(author_id=request.user)
    if request.method == 'POST':
        profile_ = ProfileForm(request.POST, instance=request.user)
        image_profile = ProfilePicsForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_.is_valid() and image_profile.is_valid():
            profile_.save()
            image_profile.save()
            return redirect('profile')
        else:
            profile_ = ProfileForm(request.POST, instance=request.user)
            image_profile = ProfilePicsForm(request.POST, request.FILES, instance=request.user.profile)
            return render(request, 'users/profile.html', {'i': img, 'profile': profile_, 'img_profile': image_profile})
    profile_ = ProfileForm(instance=request.user)
    image_profile = ProfilePicsForm(instance=request.user)
    context = {
        'i': img,
        'profile': profile_,
        'img_profile': image_profile,
        'posts': posts_user
    }
    return render(request, 'users/profile.html', context)


