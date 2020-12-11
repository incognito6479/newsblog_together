from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Posts
from users.models import Profile


def index(request):
    posts = Posts.objects.order_by('-post_added')
    prof_pics = Profile.objects.all()
    context = {
        'post': posts,
        'pics': prof_pics
    }
    return render(request, 'index.html', context)


def create_post(request):
    if request.method == 'POST':
        form_user = PostForm(request.POST)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('main:index')
    form_user = PostForm()
    context = {
        'forms': form_user
    }
    return render(request, 'post_create.html', context)
