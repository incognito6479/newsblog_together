from django.shortcuts import render, redirect
from . import models, forms


def index(request):
    posts = models.Posts.objects.order_by('-post_added')
    return render(request, 'index.html', {'post': posts})


def create_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('main:index')
    form = forms.PostForm()
    return render(request, 'post_create.html', {'form':form})
