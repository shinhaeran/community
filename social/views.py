from django.shortcuts import render, get_object_or_404, redirect
from .models import SocialPost
from .forms import SocialPostForm
from django_summernote import models as summer_model

# Create your views here.

def index(request):
    socialposts = SocialPost.objects.all

    return render(request, 'social/index.html', {
        'posts':socialposts,
    })

def new(request):
    if request.method == 'POST':
        form = SocialPostForm(request.POST)
        if form.is_valid():
            socialpost = form.save(commit=False)
            socialpost.save()
            return redirect('social:index')
    else:
        form = SocialPostForm()
    return render(request, 'social/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(SocialPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'social/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(SocialPost, pk=post_id)

    if request.method == 'POST':
        form = SocialPostForm(request.POST, instance=post)
        if form.is_valid():
            socialpost = form.save(commit=False)
            socialpost.save()
            return redirect('social:detail', post_id)
    else:
        form = SocialPostForm(instance=post)
    return render(request, 'social/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(SocialPost, pk=post_id)
    post.delete()
    return redirect('social:index')
