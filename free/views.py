from django.shortcuts import render, get_object_or_404, redirect
from .models import FreePost
from .forms import FreePostForm
from django_summernote import models as summer_model
# Create your views here.

def index(request):
    freeposts = FreePost.objects.all
    return render(request, 'free/index.html', {
        'posts':freeposts,
    })

def new(request):
    if request.method == 'POST':
        form = FreePostForm(request.POST)
        if form.is_valid():
            freepost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            freepost.save()
            return redirect('free:index')
        else:
            return redirect('free:new')
    else:
        form = FreePostForm()
    return render(request, 'free/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(FreePost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'free/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(FreePost, pk=post_id)

    if request.method == 'POST':
        form = FreePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('free:detail', post_id)
    else:
        form = FreePostForm(instance=post)
    return render(request, 'free/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(FreePost, pk=post_id)
    post.delete()
    return redirect('free:index')
