from django.shortcuts import render, get_object_or_404, redirect
from .models import NaturePost
from .forms import NaturePostForm
from django_summernote import models as summer_model

# Create your views here.

def index(request):
    natureposts = NaturePost.objects.all
    return render(request, 'nature/index.html', {
        'posts':natureposts,
    })

def new(request):
    if request.method == 'POST':
        form = NaturePostForm(request.POST)
        if form.is_valid():
            naturepost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            naturepost.save()
            return redirect('nature:index')
        else:
            return redirect('nature:new')
    else:
        form = NaturePostForm()
    return render(request, 'nature/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(NaturePost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'nature/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(NaturePost, pk=post_id)

    if request.method == 'POST':
        form = NaturePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('nature:detail', post_id)
    else:
        form = NaturePostForm(instance=post)
    return render(request, 'nature/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(NaturePost, pk=post_id)
    post.delete()
    return redirect('nature:index')
