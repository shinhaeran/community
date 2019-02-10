from django.shortcuts import render, get_object_or_404, redirect
from .models import EngineerPost
from .forms import EngineerPostForm
from django_summernote import models as summer_model

# Create your views here.

def index(request):
    engineerposts = EngineerPost.objects.all
    return render(request, 'engineer/index.html', {
        'posts':engineerposts,
    })

def new(request):
    if request.method == 'POST':
        form = EngineerPostForm(request.POST)
        if form.is_valid():
            engineerpost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            engineerpost.save()
            return redirect('engineer:index')
        else:
            return redirect('engineer:new')
    else:
        form = EngineerPostForm()
    return render(request, 'engineer/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(EngineerPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'engineer/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(EngineerPost, pk=post_id)

    if request.method == 'POST':
        form = EngineerPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('engineer:detail', post_id)
    else:
        form = EngineerPostForm(instance=post)
    return render(request, 'engineer/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(EngineerPost, pk=post_id)
    post.delete()
    return redirect('engineer:index')
