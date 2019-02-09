from django.shortcuts import render, get_object_or_404, redirect
from .models import BusinessPost
from .forms import BusinessPostForm
from django_summernote import models as summer_model

def index(request):
    businessposts = BusinessPost.objects.all
    return render(request, 'business/index.html', {
        'posts':businessposts,
    })

def new(request):
    if request.method == 'POST':
        form = BusinessPostForm(request.POST)
        if form.is_valid():
            businesspost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            businesspost.save()
            return redirect('business:index')
        else:
            return redirect('business:new')
    else:
        form = BusinessPostForm()
    return render(request, 'business/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'business/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)

    if request.method == 'POST':
        form = BusinessPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('business:detail', post_id)
    else:
        form = BusinessPostForm(instance=post)
    return render(request, 'business/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(BusinessPost, pk=post_id)
    post.delete()
    return redirect('business:index')