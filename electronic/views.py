from django.shortcuts import render, get_object_or_404, redirect
from .models import ElectronicPost
from .forms import ElectronicPostForm
from django_summernote import models as summer_model
# Create your views here.

def index(request):
    electronicposts = ElectronicPost.objects.all
    return render(request, 'electronic/index.html', {
        'posts':electronicposts,
    })

def new(request):
    if request.method == 'POST':
        form = ElectronicPostForm(request.POST)
        if form.is_valid():
            electronicpost = form.save(commit=False)     #이 부분은 아직도 모르겠다 ㅠ
            electronicpost.save()
            return redirect('electronic:index')
        else:
            return redirect('electronic:new')
    else:
        form = ElectronicPostForm()
    return render(request, 'electronic/new.html', {
        'form':form,
    })

def detail(request, post_id):
    post = get_object_or_404(ElectronicPost, pk=post_id)
    multiFile = get_object_or_404(summer_model.Attachment, id = post_id)
    return render(request, 'electronic/detail.html', {
        'post':post,
        'multiFile':multiFile,
    })

def edit(request, post_id):
    post = get_object_or_404(ElectronicPost, pk=post_id)

    if request.method == 'POST':
        form = ElectronicPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('electronic:detail', post_id)
    else:
        form = ElectronicPostForm(instance=post)
    return render(request, 'electronic/edit.html', {
        'form':form,
    })

def delete(request, post_id):
    post = get_object_or_404(ElectronicPost, pk=post_id)
    post.delete()
    return redirect('electronic:index')
