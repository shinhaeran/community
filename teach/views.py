from django.shortcuts import render, get_object_or_404, redirect
from .models import TeachPost
from .forms import TeachPostForm
from django_summernote import models as summer_model

# Create your views here.

def index(request):
    teachposts = TeachPost.objects.all

    return render(request, 'teach/index.html', {
        'posts':teachposts,
    })

def new(request):
    if request.method == 'POST':
        form = TeachPostForm(request.POST)
        if form.is_valid():
            teachpost = form.save(commit=False)
            teachpost.save()
            return redirect('teach:index')
    else:
        form = TeachPostForm()
    return render(request, 'teach/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'teach/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)

    if request.method == 'POST':
        form = TeachPostForm(request.POST, instance='post')
        if form.is_valid():
            teachpost = form.save(commit=False)
            teachpost.save()
            return redirect('teach:detail', post_id)
    else:
        form = TeachPostForm(instance=post)
    return render(request, 'teach/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(TeachPost, pk=post_id)
    post.delete()
    return redirect('teach:index')